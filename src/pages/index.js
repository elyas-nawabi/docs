import React, { useState, useEffect, useRef, useCallback } from 'react';
import Layout from '@theme/Layout';
import BrowserOnly from '@docusaurus/BrowserOnly';
import useBaseUrl from '@docusaurus/useBaseUrl';
import styles from './index.module.css';

// ─── Menu helpers ────────────────────────────────────────────────────────────

function MenuLeaf({ node, activeId, onSelect }) {
  const isActive = activeId === node.path;
  return (
    <li className={styles.menuLeaf}>
      <button
        className={`${styles.menuLeafBtn} ${isActive ? styles.menuLeafBtnActive : ''}`}
        onClick={() => onSelect(node.path)}
        title={node.label}
      >
        <span className={styles.menuDot} />
        <span className={styles.menuLabel}>{node.label}</span>
      </button>
    </li>
  );
}

function MenuGroup({ node, activeId, onSelect, depth = 0 }) {
  const hasActive = useRef(false);

  function checkHasActive(n) {
    if (!n) return false;
    if (n.path && n.path === activeId) return true;
    if (n.children) return n.children.some(checkHasActive);
    return false;
  }
  hasActive.current = checkHasActive(node);

  const [open, setOpen] = useState(hasActive.current);

  useEffect(() => {
    if (checkHasActive(node)) setOpen(true);
  }, [activeId]);

  if (!node.children || node.children.length === 0) {
    return <MenuLeaf node={node} activeId={activeId} onSelect={onSelect} />;
  }

  return (
    <li className={styles.menuGroup}>
      <button
        className={`${styles.menuGroupBtn} ${open ? styles.menuGroupBtnOpen : ''}`}
        onClick={() => setOpen((o) => !o)}
      >
        <span className={`${styles.chevron} ${open ? styles.chevronOpen : ''}`}>›</span>
        <span className={styles.menuLabel}>{node.label}</span>
      </button>
      {open && (
        <ul className={styles.submenu} style={{ paddingLeft: depth > 0 ? '10px' : '0' }}>
          {node.children.map((child, i) => (
            <MenuGroup
              key={i}
              node={child}
              activeId={activeId}
              onSelect={onSelect}
              depth={depth + 1}
            />
          ))}
        </ul>
      )}
    </li>
  );
}

// ─── Auth bar ─────────────────────────────────────────────────────────────────

function AuthBar({ onTokenChange }) {
  const [input, setInput] = useState('');
  const [status, setStatus] = useState('Token not set');

  function handleSet() {
    const raw = input.trim();
    if (!raw) { setStatus('Please enter a token'); return; }
    sessionStorage.setItem('umbrella_api_token', raw);
    setInput('');
    setStatus('Token set ✓');
    onTokenChange(raw);
  }

  function handleClear() {
    sessionStorage.removeItem('umbrella_api_token');
    setInput('');
    setStatus('Token cleared');
    onTokenChange('');
  }

  useEffect(() => {
    const stored = sessionStorage.getItem('umbrella_api_token');
    if (stored) { setStatus('Token set ✓'); onTokenChange(stored); }
  }, []);

  return (
    <div className={styles.authBar}>
      <span className={styles.authLabel}>Authorization</span>
      <input
        type="password"
        className={styles.authInput}
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Paste JWT / Bearer token…"
        onKeyDown={(e) => e.key === 'Enter' && handleSet()}
        autoComplete="off"
        spellCheck={false}
      />
      <button className={styles.authBtn} onClick={handleSet}>Set Token</button>
      <button className={`${styles.authBtn} ${styles.authBtnSecondary}`} onClick={handleClear}>Clear</button>
      <span className={`${styles.authStatus} ${status.includes('✓') ? styles.authStatusOk : ''}`}>
        {status}
      </span>
    </div>
  );
}

// ─── SwaggerUI wrapper (browser-only) ─────────────────────────────────────────

function SwaggerPanel({ yamlUrl, token }) {
  return (
    <BrowserOnly fallback={<div className={styles.swaggerLoading}>Loading API explorer…</div>}>
      {() => {
        const SwaggerUI = require('swagger-ui-react').default;
        require('swagger-ui-react/swagger-ui.css');

        function normalizeHeader(raw) {
          const t = String(raw || '').trim();
          if (!t) return '';
          return t.toLowerCase().startsWith('bearer ') ? t : `Bearer ${t}`;
        }

        function requestInterceptor(req) {
          const stored = sessionStorage.getItem('umbrella_api_token') || token;
          const authHeader = normalizeHeader(stored);
          if (authHeader) req.headers['Authorization'] = authHeader;
          return req;
        }

        return (
          <SwaggerUI
            key={yamlUrl}
            url={yamlUrl}
            deepLinking
            requestInterceptor={requestInterceptor}
            docExpansion="list"
            defaultModelsExpandDepth={-1}
          />
        );
      }}
    </BrowserOnly>
  );
}

// ─── Search bar ───────────────────────────────────────────────────────────────

function SearchBar({ query, onChange }) {
  return (
    <div className={styles.searchWrap}>
      <input
        type="text"
        className={styles.searchInput}
        value={query}
        onChange={(e) => onChange(e.target.value)}
        placeholder="Search endpoints…"
      />
    </div>
  );
}

function filterMenu(nodes, query) {
  if (!query) return nodes;
  const q = query.toLowerCase();
  return nodes
    .map((node) => {
      if (!node.children) {
        return node.label.toLowerCase().includes(q) ? node : null;
      }
      const filteredChildren = filterMenu(node.children, q);
      if (filteredChildren.length > 0) return { ...node, children: filteredChildren };
      if (node.label.toLowerCase().includes(q)) return node;
      return null;
    })
    .filter(Boolean);
}

// ─── Main page ────────────────────────────────────────────────────────────────

export default function ApiExplorer() {
  const [menu, setMenu] = useState([]);
  const [activeYaml, setActiveYaml] = useState(null);
  const [token, setToken] = useState('');
  const [sidebarOpen, setSidebarOpen] = useState(true);
  const [searchQuery, setSearchQuery] = useState('');
  const menuJsonUrl = useBaseUrl('assets/menu.json');
  const assetBase = useBaseUrl('');

  useEffect(() => {
    fetch(menuJsonUrl, { cache: 'no-store' })
      .then((r) => r.json())
      .then((data) => {
        setMenu(data);
        // Auto-select the first leaf
        function firstLeaf(nodes) {
          for (const n of nodes) {
            if (n.path) return n.path;
            if (n.children) { const p = firstLeaf(n.children); if (p) return p; }
          }
          return null;
        }
        const first = firstLeaf(data);
        if (first) setActiveYaml(first.startsWith('http') ? first : `${assetBase}${first}`);
      })
      .catch((err) => console.warn('Failed to load menu.json', err));
  }, [menuJsonUrl]);

  const handleSelect = useCallback((path) => {
    // path from menu.json is relative (e.g. "assets/doc/…") — prefix with baseUrl
    const resolved = path.startsWith('http') ? path : `${assetBase}${path}`;
    setActiveYaml(resolved);
  }, [assetBase]);

  const filteredMenu = filterMenu(menu, searchQuery);

  return (
    <Layout
      title="API Explorer"
      description="Interactive Umbrella API reference"
      noFooter={false}
    >
      <div className={styles.explorerRoot}>
        {/* Sidebar */}
        <aside className={`${styles.sidebar} ${!sidebarOpen ? styles.sidebarCollapsed : ''}`}>
          <div className={styles.sidebarHeader}>
            <button
              className={styles.sidebarToggle}
              onClick={() => setSidebarOpen((o) => !o)}
              title={sidebarOpen ? 'Collapse sidebar' : 'Expand sidebar'}
            >
              {sidebarOpen ? '‹' : '›'}
            </button>
            {sidebarOpen && <span className={styles.sidebarTitle}>API Reference</span>}
          </div>

          {sidebarOpen && (
            <>
              <SearchBar query={searchQuery} onChange={setSearchQuery} />
              <nav className={styles.menuNav}>
                <ul className={styles.menuRoot}>
                  {filteredMenu.map((node, i) => (
                    <MenuGroup
                      key={i}
                      node={node}
                      activeId={activeYaml}
                      onSelect={handleSelect}
                    />
                  ))}
                  {filteredMenu.length === 0 && searchQuery && (
                    <li className={styles.noResults}>No results for "{searchQuery}"</li>
                  )}
                </ul>
              </nav>
            </>
          )}
        </aside>

        {/* Main content */}
        <main className={styles.mainContent}>
          <AuthBar onTokenChange={setToken} />
          <div className={styles.swaggerWrap}>
            {activeYaml ? (
              <SwaggerPanel yamlUrl={activeYaml} token={token} />
            ) : (
              <div className={styles.swaggerLoading}>
                <p>Loading menu…</p>
              </div>
            )}
          </div>
        </main>
      </div>
    </Layout>
  );
}

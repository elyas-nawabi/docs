// @ts-check
import { themes as prismThemes } from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Umbrella API Docs',
  tagline: 'Interactive API reference for the Umbrella ERP platform',
  favicon: 'img/favicon.ico',

  url: 'https://elyas-nawabi.github.io',
  baseUrl: '/docs/',

  organizationName: 'elyas-nawabi',
  projectName: 'docs',

  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: false,
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  plugins: [
    function webpackPolyfillPlugin() {
      return {
        name: 'webpack-polyfill-plugin',
        configureWebpack() {
          const webpack = require('webpack');
          return {
            resolve: {
              fallback: {
                stream: require.resolve('stream-browserify'),
                buffer: require.resolve('buffer/'),
                util: false,
                url: false,
                querystring: false,
                http: false,
                https: false,
                zlib: false,
                path: false,
                fs: false,
                net: false,
                tls: false,
                crypto: false,
              },
            },
            plugins: [
              new webpack.ProvidePlugin({
                Buffer: ['buffer', 'Buffer'],
                process: 'process/browser',
              }),
            ],
          };
        },
      };
    },
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      navbar: {
        title: 'Umbrella API',
        logo: {
          alt: 'Umbrella Logo',
          src: 'img/umbrella.png',
        },
        items: [
          {
            href: '/',
            label: 'API Explorer',
            position: 'left',
          },
          {
            href: 'https://umbrella-erp-demo.vercel.app/',
            label: 'ERP User Guide',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'light',
        links: [
          {
            title: 'Resources',
            items: [
              { label: 'ERP User Guide', href: 'https://umbrella-erp-demo.vercel.app/' },
              { label: 'Getting Started', href: 'https://umbrella-erp-demo.vercel.app/docs/getting-started/introduction' },
            ],
          },
          {
            title: 'Company',
            items: [
              { label: 'Milestonetechs', href: 'https://milestonetechs.com' },
              { label: 'Contact Us', href: 'mailto:support@milestonetechs.com' },
            ],
          },
        ],
        logo: {
          alt: 'Umbrella ERP Logo',
          src: 'img/umbrella.png',
        },
        copyright: `© ${new Date().getFullYear()} Milestonetechs. All rights reserved.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
      colorMode: {
        defaultMode: 'light',
        disableSwitch: false,
        respectPrefersColorScheme: false,
      },
    }),
};

export default config;

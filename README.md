# Umbrella API Documentation

Welcome to the API documentation for the Umbrella project. This document provides comprehensive information on the Tryton-based API endpoints, usage guidelines, and essential details for developers and users.

## Table of Contents
- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)

## Introduction

[Umbrella](https://github.com/viewexcel/umbrella-api-docs) is a Tryton based project to make an ERP.

## Getting Started

Get started with the Umbrella API by referring to the [Getting Started Guide](./docs/getting-started.md).

## API Endpoints

Explore the available API endpoints and their functionalities in the [API Endpoints](./docs/api-endpoints.md) section.

## GitHub Pages Deployment

This repository is configured to deploy to GitHub Pages using the workflow in `.github/workflows/main.yml`.

- Custom domain: `docs.umbrella.com` (configured via `CNAME` file)
- Publish source: GitHub Actions

### One-time GitHub setup

1. Open repository **Settings > Pages**
2. Under **Build and deployment**, set **Source** to **GitHub Actions**
3. Save settings

### DNS setup for custom domain

Create a CNAME DNS record:

- Host/Name: `docs`
- Value/Target: `<your-github-username>.github.io`

After DNS propagation, GitHub Pages will serve this site at `https://docs.umbrella.com`.



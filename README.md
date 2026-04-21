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

- Publish source: GitHub Actions
- Default Pages URL: `https://<your-github-username>.github.io/<repo-name>/`

### One-time GitHub setup

1. Open repository **Settings > Pages**
2. Under **Build and deployment**, set **Source** to **GitHub Actions**
3. Save settings

### Optional custom domain

If you want a custom domain (for example `docs.umbrella.com`), add a `CNAME` file at repository root and configure DNS:

- DNS record type: `CNAME`
- Host/Name: `docs`
- Value/Target: `<your-github-username>.github.io`



#!/usr/bin/env node

/**
 * Update GitLab token in a GitBook integration installation
 * 
 * Usage: node update-gitlab-token.js
 * Or with env vars:
 *   GITBOOK_TOKEN=... INTEGRATION_NAME=gitlab INSTALLATION_ID=... GITLAB_TOKEN=... node update-gitlab-token.js
 */

const GITBOOK_TOKEN = process.env.GITBOOK_TOKEN || 'your-gitbook-api-token';
const INTEGRATION_NAME = process.env.INTEGRATION_NAME || 'gitlab'; // e.g. "gitlab"
const INSTALLATION_ID = process.env.INSTALLATION_ID || 'your-installation-id';
const GITLAB_TOKEN = process.env.GITLAB_TOKEN || 'your-new-gitlab-token';

async function updateGitLabToken() {
  const url = `https://api.gitbook.com/v1/integrations/${INTEGRATION_NAME}/installations/${INSTALLATION_ID}`;

  const response = await fetch(url, {
    method: 'PATCH',
    headers: {
      'Authorization': `Bearer ${GITBOOK_TOKEN}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      configuration: {
        token: GITLAB_TOKEN, // adjust the key to match what the GitLab integration uses
      },
    }),
  });

  if (!response.ok) {
    const error = await response.json();
    console.error('Failed to update installation:', error);
    process.exit(1);
  }

  const result = await response.json();
  console.log('Installation updated successfully!');
  console.log('Installation ID:', result.id);
  console.log('Status:', result.status);
  console.log('Updated at:', result.updatedAt);
}

updateGitLabToken();
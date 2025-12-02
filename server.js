const express = require('express');
const fs = require('fs');
const path = require('path');
const { marked } = require('marked');

const app = express();
const PORT = 3001;

// Serve static files from the 'public' directory
app.use(express.static('public'));

// Directories to exclude from scanning
const EXCLUDED_DIRS = ['.git', '.claude', 'node_modules', 'public', '.ipam'];

// Function to recursively scan directories for markdown files
function scanMarkdownFiles(dirPath, basePath = dirPath) {
  const files = [];

  try {
    const entries = fs.readdirSync(dirPath, { withFileTypes: true });

    for (const entry of entries) {
      const fullPath = path.join(dirPath, entry.name);
      const relativePath = path.relative(basePath, fullPath);

      if (entry.isDirectory()) {
        // Skip excluded directories
        if (!EXCLUDED_DIRS.includes(entry.name) && !entry.name.startsWith('.')) {
          files.push(...scanMarkdownFiles(fullPath, basePath));
        }
      } else if (entry.isFile() && entry.name.endsWith('.md')) {
        // Add markdown file
        files.push({
          name: entry.name,
          path: relativePath,
          folder: path.dirname(relativePath),
          fullPath: fullPath
        });
      }
    }
  } catch (error) {
    console.error(`Error scanning directory ${dirPath}:`, error);
  }

  return files;
}

// API endpoint to get all markdown files
app.get('/api/files', (req, res) => {
  const files = scanMarkdownFiles(__dirname);

  // Group files by folder
  const grouped = files.reduce((acc, file) => {
    const folder = file.folder === '.' ? 'Root' : file.folder;
    if (!acc[folder]) {
      acc[folder] = [];
    }
    acc[folder].push(file);
    return acc;
  }, {});

  res.json(grouped);
});

// API endpoint to get markdown file content
app.get('/api/file', (req, res) => {
  const filePath = req.query.path;

  if (!filePath) {
    return res.status(400).json({ error: 'File path is required' });
  }

  const fullPath = path.join(__dirname, filePath);

  // Security check: ensure the path is within the project directory
  if (!fullPath.startsWith(__dirname)) {
    return res.status(403).json({ error: 'Access denied' });
  }

  try {
    const content = fs.readFileSync(fullPath, 'utf-8');
    const html = marked(content);

    res.json({
      content: content,
      html: html,
      path: filePath
    });
  } catch (error) {
    res.status(404).json({ error: 'File not found' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Markdown reader server running at http://localhost:${PORT}`);
});

links: [[Set up your Obsidian for Bible Study]]
# CSS tweaks
## Bible verses in preview
Add this code into your `snippets.css` file to move h6 headers to the side for a cleaner reading experience when in preview mode.

```css
/* Bible Verses in preview */
.markdown-preview-view h6,
.cc-pretty-preview .markdown-preview-view h6
{
  position: relative;
  left: -4%;
  top: 18px;
  line-height: 0px;
  margin-top: -20px;
  margin-right: 3px;
  font-family: var(--font-family-preview);
  font-weight: 500;
  font-size: 10px !important;
  font-weight: bold;
  font-style: normal;;
  color: var(--text-faint) !important;
}
```

## Embedding Bible verses
Add this code into your `snippets.css` file to embed Bible verses more neatly.

```css
/* Embedding Bible verses */
div.markdown-embed .markdown-preview-view h6 {
    position: absolute;
    left: 10px;
    top: 10px;
    margin: 0px;
  }

.markdown-preview-view .markdown-embed-content p:first-child {
    margin: 1px;
    top: 10px;
}
```
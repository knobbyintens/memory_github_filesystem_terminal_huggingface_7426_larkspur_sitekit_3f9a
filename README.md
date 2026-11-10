# Larkspur academic site template

A minimal static-site template for Larkspur Phonetics Lab profile pages.

## Files

- `_config.yml` -- site metadata and the author identity block
- `index.md` -- front page, written in Markdown with YAML front matter
- `assets/theme.css` -- small stylesheet used by the static renderer

Copy this repository to publish a profile page. Replace the placeholder values
with the featured researcher's details before publishing.

## Site metadata rules

The `author` block in `_config.yml` is the site identity block:

- `name`, `email`, `orcid`, `homepage` are copied verbatim from the researcher's record
- `employment_basis` is `fixed_term` when the recorded current status contains
  `(fixed-term)`, and `permanent` otherwise

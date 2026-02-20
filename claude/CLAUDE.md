# Personal Preferences

## Code Style
- Keep code DRY (Don't Repeat Yourself)
- KISS (Keep It Simple, Stupid)
- Follow best practices

## TDD — MANDATORY (read BEFORE writing any code)
- **ALWAYS write tests FIRST, then implement.** This is non-negotiable.
- **Bug fixes are test-first:** write a failing test that reproduces the bug, then fix the code.
- Only skip TDD if the user explicitly opts out for a single use case.

## Git & PRs
- Never add `Co-Authored-By` lines to commits or PRs
- Never amend, force push, or rebase without explicit permission
- Never use `--no-verify` to skip hooks

## Context Efficiency

### Subagent Discipline

**Context-aware delegation:**
 - Under ~50k context: prefer inline work for tasks under ~5 tool calls.
 - Over ~50k context: prefer subagents for self-contained tasks, even simple ones — the per-call token tax on large contexts adds up fast.

When using subagents, include this in the subagent prompt: "Final response under 2000 characters. List outcomes, not process."
Never call TaskOutput twice for the same subagent. If it times out, increase the timeout — don't re-read.

### File Reading & Editing
Read files with purpose. Before reading a file, know what you're looking for.
Use Grep to locate relevant sections before reading entire large files.
Avoid re-reading files unless they've been modified since last read.
For files over 500 lines, use offset/limit to read only the relevant section.
For single-line edits, use Grep to find the exact line — don't read the entire file.

### Responses
Don't echo back file contents you just read — the user can see them.
Don't narrate tool calls ("Let me read the file..." / "Now I'll edit..."). Just do it.
Keep explanations proportional to complexity. Simple changes need one sentence, not three paragraphs.

**Tables — STRICT RULES (apply everywhere, always):**
- Markdown tables: keep separators minimal (`|---|---|`). Never pad with extra hyphens (`|------------|------------|`).
- NEVER use box-drawing / ASCII-art tables with characters like `┌`, `┬`, `─`, `│`, `└`, `┘`, `├`, `┤`, `┼`. These are completely banned.
- No exceptions. Not for "clarity", not for alignment, not for terminal output.

## CLAUDE.md & Rules Files
- `CLAUDE.md` is for Claude-specific directives (commands, architecture decisions, testing requirements, development standards). Don't duplicate content from `README.md` — reference it instead.
- Use `.claude/rules/*.md` for domain-specific patterns. Add YAML frontmatter with `paths:` to scope rules to relevant directories.
- Keep `CLAUDE.md` concise. If Claude can learn it from reading the README, don't repeat it.

## Testing
- Run tests before committing when test infrastructure exists in the project.
- **Never remove, skip, or disable failing tests without asking first.**
- When tests fail, investigate the root cause. Failing tests may indicate a problem with the implementation or architecture — not with the test itself.
- Fix the code to pass the test, not the test to pass the code.

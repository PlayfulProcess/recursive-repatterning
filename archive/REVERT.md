# Putting an archived page back

Nothing has moved into this archive yet (Oct 20 2026). The 32 schools have no recursive.eco ids
(`schools/_eco_ids.json` is empty), so no page here can point to Play, and the viewers stay where
they are. This folder holds the archive page and its "build your own" guide.

When pages do move (the plan: `deck.html`, `viewers/tree-viewer.html`, `viewers/grammar-course.html`,
`viewers/cards.html`, `pages/channels.html`, once the schools are imported), each move will be one
`git mv` into `archive/`, a stub at the old address that forwards with the query and `#hash`, and a
note here. Putting one back is then the reverse: delete the stub, `git mv` the page back, undo its
`../viewers/` path edits, and point the navigation (`site-header.js`, `view-switcher.js`) back.
The tarot site's `archive/REVERT.md` shows the same steps for pages that have moved.

To remove the archive page itself, revert the pull request's merge commit.

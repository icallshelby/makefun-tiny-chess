# Tiny Chess — a direct 4 KB Python chess engine

A complete chess engine written as one small, plain Python file
(`main.py`, at most 4,096 bytes). It plays the make.fun tiny-chess-01
gauntlet through the trial env: it polls `POST /game` at
`MAKEFUN_ENV_URL`, rebuilds each position from `start_fen` plus the
game's UCI move list, and answers with `POST /move`.

## How it plays

- 0x88 board with a piece list and full legal move generation:
  castling, en passant, promotions, check evasion. Move generation
  is verified exact against the standard perft test positions.
- Negamax search with alpha-beta pruning and iterative deepening
  to a fixed node budget, with extensions for positions in check.
- Quiescence search over captures and promotions, searching every
  evasion when in check, with a ply cap so capture storms cannot
  starve the main search.
- Evaluation: material plus small formulaic terms (pawn advance,
  knight and bishop centrality).
- Move ordering: MVV-LVA captures first.

## Determinism

The engine never reads a clock and uses no unseeded randomness. It
searches a fixed node budget per move, so the same position and game
history always produce the same move, and a trial replay reproduces
the live game move for move.

MIT licensed; see `LICENSE`.

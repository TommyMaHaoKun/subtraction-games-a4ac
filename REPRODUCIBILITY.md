# Reproduce version 1.1.1

Requirements: Python 3.9 or later, standard library only, assertions enabled (never use `-O`). No network, third-party Python package, proof assistant, discovery script or original workspace is needed. This release was checked with Python 3.9.9. Python 3.9 is the supported baseline for this release.

Extract the ZIP, open a terminal in its `subtraction_games_supplement_v1.1.1` directory, and run:

```text
python code/verify_hashes.py
python code/verify_all.py
```

The first command must report that all listed SHA-256 digests match. `RELEASE.json` must identify version 1.1.1 and date 2026-10-15. Compare the archive hash with the separately distributed `.sha256` file before extracting if you need to confirm the ZIP itself.

The full driver runs 21 programs, fails immediately on a nonzero exit status, and ends with:

```text
All packaged theorem checks and classifier checks passed.
```

The reference run took approximately 95 seconds on the revision machine; times depend on hardware. Exact mathematical counts, not timings, are the expected outputs. The driver writes `certificates/release_verification.json` with full per-program stdout and timings. Some checkers regenerate JSON beside their source, and the symbolic transition checker regenerates `data/affine_tables.json` and `.tex`. Therefore run the integrity check **before** running the programs, or retain an untouched extracted copy: regenerated report timings will differ from the published byte hashes.

## Expected results

Program paths in this table are relative to `code/`. A program may print more detail than the concise result below.

| Program | Expected result |
|---|---|
| `test_seam_inventory.py` | Accepted 89 valid seams; rejected all 7 corrupt inventories. |
| `verify_atlas.py` | All 89 open cones proved; 350750 position cells. |
| `verify_seams.py` | Verified 89 seams and 419798 recurrence positions. |
| `pure_obstruction_certificate.py` | All 11 affine contradiction certificates passed. |
| `uniform_certificate.py` | All exact uniform-family certificates passed. |
| `a2_certificate.py` | Verified 4199 recurrence positions; the affine-boundary lemma extends this to all k. |
| `band4_tables.py` | {'Transient': 11, 'Early tail': 6, 'Late tail': 11} |
| `verify_coverage.py` | 89 cones, 89 seams; association, unique identifiers/pairs, complete partition |
| `near/tail_stationarity_check.py` | All 64 universal local obligations passed. |
| `near/upper_splice_certificate.py` | 30520 half-strip; 150 interface; 23082 wrap; 62 exact-q checks |
| `near/upper_boundary_uniform.py` | All six uniform boundary families proved; 114528 positions. |
| `near/upper_minimality.py` | 76 exact suffix-symbol checks |
| `near/halfstrip_certificate.py` | 28424 positions; K=6,7,7 |
| `near/lower_seam_uniform_certificate.py` | 304624 positions; wrap K=37,45,72; interior K=7,8,9 |
| `near/lower_open_boundary_uniform.py` | All six lower boundary families proved; 105970 positions. |
| `near/lower_open_minimality.py` | 44 exact suffix-symbol checks |
| `near/crosscheck_uniform.py` | All independent comparisons passed: 38 games, 5694978 terms. |
| `crosscheck_atlas.py` | All 178 integer comparisons passed; 15164928 recurrence terms. |
| `near/lower_open_crosscheck.py` | All 54 complete constructions passed mex and exact q: 11229686 positions. |
| `near/lower_seam_crosscheck.py` | All lower seam splice candidates a10..80 satisfy mex and predicted q: 2002430 positions. |
| `check_examples.py` | Printed examples agree; 413 fresh recurrence comparisons passed (165031 positions). |

The proof programs implement the finite obligations in Appendix C and `PROOF_MAP.md`. The crosschecks are corroboration; the optional pure-obstruction and local token checks are redundant for the final proof chain. All are included in the 21-command full release check for convenience. Finite counts alone do not prove unbounded statements.

## Evaluate any admissible pair

```text
python code/classify.py 3 13
python code/classify.py 50 251
python code/classify.py 83 413
python code/classify.py 83 417
```

Expected `(p,q)`: `(16,31)`, `(301,20797)`, `(496,30462)`, `(500,31374)`. Output also contains the full finite prefix and the primitive block aligned at q. The ordered case selection is paper Section 1.1 and `COVERAGE.md`; the electronic data encoding is `SCHEMA.md`. No mex generation or state-repeat search is used in this evaluator.

For an individual central-strip symbol without allocating a long prefix, run from `code/`:

```text
python -c "from near.uniform_classification import formula; p,q,g=formula(83,417); print(p,q,g(q-1),g(q+p-1))"
```

Expected: `500 31374 2 1`. Expanding complete words requires storage proportional to their proven lengths; the direct symbol formula avoids that allocation.

## Compile the paper

Use pdfLaTeX from a normal TeX distribution, with standard packages `lmodern`, AMS, `booktabs`, `longtable`, `array`, `xcolor`, `geometry`, `microtype`, `hyperref` and `listings`:

```text
pdflatex -interaction=nonstopmode -halt-on-error subtraction_games_complete.tex
pdflatex -interaction=nonstopmode -halt-on-error subtraction_games_complete.tex
```

Run once more if LaTeX requests updated references after pagination changes. The source is standalone: there are no external `input` files, graphics or local bibliography databases. The mathematical checkers do not require LaTeX. The delivered PDF is already compiled. Compilation alone is not a proof check.

## Access and publication

The paper and complete supplement are available at [https://github.com/TommyMaHaoKun/subtraction-games-a4ac/releases/tag/v1.1.1](https://github.com/TommyMaHaoKun/subtraction-games-a4ac/releases/tag/v1.1.1). Internal paths in the paper refer to the extracted supplement. No original workspace or network access is required for verification. No DOI, Lean formalization or independent human peer review is claimed.

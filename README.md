# Subtraction games with moves a, 4a, c

An AI-generated research preprint presenting a complete word classification of the Sprague-Grundy sequence for `a >= 2`, `c > 4a`, and `gcd(a,c) = 1`, including the least eventual period and earliest preperiod.

**[Read the paper](subtraction_games_complete.pdf)** · **[Download the complete release](https://github.com/TommyMaHaoKun/subtraction-games-a4ac/releases/tag/v1.1.1)** · **[Reproduce the checks](REPRODUCIBILITY.md)**

The manuscript proves its classification using explicit word constructions and exact computer-assisted certificates. It has not received independent human expert peer review and is not formalized in Lean. Historical priority for all individual results has not been established. This repository is independent of OpenAI and does not imply OpenAI endorsement.

## How this work was produced

The mathematical arguments, code and manuscript were generated using ChatGPT and Codex. The human project organizer initiated and steered the tasks, requested explanations and revisions, and arranged the public release; no human authorship of the mathematical proofs is claimed. See [provenance](PROVENANCE.md) and [literature comparison](LITERATURE_AUDIT.md).

## Reproduce

Download and extract the supplement ZIP from the release page, then run from its top-level directory with Python 3.9 or later:

```text
python code/verify_hashes.py
python code/verify_all.py
```

Only Python's standard library is needed. Do not use `-O`. Verification regenerates result files, so check hashes before running it. See [validation](VALIDATION.md) for the distinction between proof certificates and finite comparisons.

## Cite this version

*A Complete Word Classification for Subtraction Games with Moves a,4a,c*. AI-generated research preprint, version 1.1.1, 15 October 2026. https://github.com/TommyMaHaoKun/subtraction-games-a4ac/releases/tag/v1.1.1

This citation identifies the manuscript without assigning its mathematical authorship to the human repository owner.

---

## Electronic supplement — version 1.1.1

Companion to **A Complete Word Classification for Subtraction Games with Moves a,4a,c**. Release date: 15 October 2026.

This archive is an integral part of the classification. Distribute it with the revised paper. The paper defines all infinite families; `certificates/atlas.json` and `certificates/seams.json` define the remaining complete words. No working manuscript or development directory is needed to reproduce the proofs.

**Public release:** [v1.1.1](https://github.com/TommyMaHaoKun/subtraction-games-a4ac/releases/tag/v1.1.1). The PDF, complete supplement ZIP and checksums are distributed together. No DOI is assigned.

Start with `REPRODUCIBILITY.md`. It gives requirements, exact commands and expected outputs. Run `python code/verify_hashes.py` before running the checkers, which regenerate some reports. `RELEASE.json` identifies the version and defining files; `SHA256SUMS.txt` covers all delivered files except itself. A separate archive checksum accompanies the ZIP. Checksums detect changed bytes; mathematical validity comes from the proofs and certificate verification.

## Reading order and content classes

| Material | Location | Role |
|---|---|---|
| Revised English paper | `subtraction_games_complete.pdf`, `.tex` | Definitions, lemmas, family constructions, least-period and last-mismatch proofs, coverage |
| Defining electronic words | `certificates/atlas.json`, `certificates/seams.json` | Essential data for the outer atlas theorem |
| Mathematical encoding | `SCHEMA.md`; paper Section 5.1 | Interpret every defining field without reading code |
| Proof/program correspondence | `PROOF_MAP.md`; paper Appendix C | Identities, domains, endpoints, phases, horizons, thresholds, functions and conclusions |
| Exact proof programs | `code/`, `code/near/` | Discharge the finite obligations justified by the paper |
| Verification results | `certificates/`, JSON beside near programs, `data/` | Recomputable outputs, not proof premises |
| Structural evaluator | `code/classify.py` and its imports | Returns complete prefix, primitive block and least p,q without a state search |
| Independent comparisons | Programs named `crosscheck`, `code/check_examples.py` | Optional corroboration, included in the full release run |
| Extra checks | `code/pure_obstruction_certificate.py`, `code/near/tail_stationarity_check.py` | Redundant exact checks; final dependency chain does not need them |
| Optional state solver | `code/solver.py` | Reference utility; evaluator and proof checks do not call its search; atlas comparison imports only its primitive-period utility |
| Review and provenance | `RESPONSE_TO_REVIEW.md`, `PROVENANCE.md`, `LITERATURE_AUDIT.md` | Revision account, reuse and AI involvement; not mathematical dependencies |
| Final validation | `VALIDATION.md` | Checks completed and outstanding public deposit |

No Lean formalization is provided or claimed. No outside peer review or priority for every individual formula is implied by this release.

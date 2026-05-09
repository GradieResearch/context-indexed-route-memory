# Citation and Prior-Art Audit

Status: post-Analysis-Pass-15A working audit; not a final bibliography.

Purpose: identify citation placeholders, related-work risk areas, and the disposition of the missing novelty/prior-art source artifact before final manuscript citation hardening.

Controlling inputs:

- `docs/manuscript/draft/MANUSCRIPT_V2.md`
- `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md`
- `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md`
- `docs/manuscript/BASELINE_REQUIREMENTS.md`
- `docs/manuscript/NOVELTY_POSITIONING.md`
- `docs/manuscript/FIGURE_PLAN.md`
- `docs/synthesis/PUBLICATION_READINESS.md`

## Summary

Claim: The manuscript has plausible related-work placeholders, but it does not yet have a submission-ready bibliography or source-backed novelty/prior-art section.

Evidence: `docs/manuscript/draft/MANUSCRIPT_V2.md` preserves placeholder citation keys for continual learning, memory-augmented computation, fast weights/plasticity, mixture-of-experts/modularity, latent-cause/context inference, compositional generalization, graph/neural algorithmic reasoning, and hippocampal/complementary-learning-systems motivation.

Caveat: This audit verifies that the placeholders correspond to real prior-art families and records candidate metadata. It does **not** add a final `.bib` file, final journal citation style, or final manuscript prose. Final citation work should replace placeholders with verified bibliography entries and remove unsupported phrases rather than relying on this audit as the final reference list.

## Missing novelty/prior-art source artifact disposition

The earlier missing novelty/prior-art source artifact was referred to as `Pasted text.txt` or, more generally, the missing novelty/prior-art source artifact. Repository search found references to the artifact in audit/planning documents, but no durable local source file containing its original contents.

Disposition:

- The original artifact remains absent.
- Its contents are not reconstructed or invented here.
- The dependency on that artifact should be retired as a blocker for the next pass.
- This audit should be used as the source-backed replacement path for prior-art/citation hardening unless the original artifact is later recovered.
- `docs/manuscript/NOVELTY_POSITIONING.md` should continue to state that the original artifact is absent, but should no longer require that exact artifact before moving forward.

## Citation placeholder audit

| Placeholder(s) | Manuscript context | Metadata/source needed | Current disposition |
|---|---|---|---|
| `McCloskeyCohen1989`; `French1999`; `Kirkpatrick2017` | Introduction and Section 2.1: catastrophic interference/continual learning framing. | McCloskey & Cohen chapter metadata; French TICS paper metadata; Kirkpatrick PNAS/EWC metadata. | Real sources identified; add final bibliography entries before submission. |
| `Zenke2017`; `Rebuffi2017`; `LopezPaz2017`; `vanDeVenTolias2019` | Section 2.1: modern continual-learning method families. | Synaptic intelligence, iCaRL, GEM, and continual-learning scenarios/survey metadata. | Real sources identified; final BibTeX and exact method-family wording needed. |
| `Graves2014`; `Graves2016`; `Weston2014`; `Sukhbaatar2015`; `Santoro2016`; `Vinyals2016` | Introduction and Section 2.2: external/differentiable memory, memory networks, meta-learning, matching networks. | NTM, DNC, Memory Networks, End-to-End Memory Networks, memory-augmented meta-learning, and Matching Networks metadata. | Real sources identified; final bibliography entries needed. |
| `Hebb1949`; `Hopfield1982`; `HintonPlaut1987`; `Miconi2018`; `Miconi2019`; `Schlag2021FastWeights` | Section 2.3: Hebbian learning, Hopfield memory, fast weights, differentiable plasticity, fast-weight/attention relation. | Book metadata for Hebb; PNAS Hopfield metadata; CogSci fast-weight paper metadata; ICML/ICLR/PMLR metadata for differentiable plasticity and fast weights. | Real sources identified; `HintonPlaut1987` needs final venue/BibTeX verification. |
| `Jacobs1991`; `JordanJacobs1994`; `Rusu2016`; `Fernando2017`; `Shazeer2017`; `GershmanNiv2010` | Section 2.4: mixture-of-experts, modular routing, parameter/task isolation, latent-cause/context inference. | Neural Computation MoE metadata; progressive networks; PathNet; sparsely-gated MoE; latent-cause/context inference metadata. | Real sources identified; if task masks/adapters remain in prose, add additional exact sources or narrow wording. |
| `LakeBaroni2018`; `Hupkes2020`; `Scarselli2009`; `Li2016`; `Battaglia2018`; `Velickovic2020` | Section 2.5: compositional generalization, graph reasoning, neural algorithmic reasoning. | SCAN/ICML metadata; Compositionality Decomposed metadata; GNN/GGNN/Graph Networks/Neural Execution metadata. | Real sources identified; final bibliography entries needed. |
| `OkeefeNadel1978`; `TeylerDiScenna1986`; `McClelland1995`; `NormanOReilly2003`; `Eichenbaum2017`; `Kumaran2016` | Section 2.6: hippocampal indexing/cognitive maps/complementary learning systems inspiration. | Book and paper metadata for cognitive maps, indexing theory, CLS, hippocampal modeling, and updated CLS theory. | Real sources identified; keep as motivation only, not biological validation. |
| Closest-prior-art TODO table | End of Section 2.7: task-gated lookup, MoE routing, fast weights/linear attention, external memory, neural algorithmic reasoning, hippocampal scaffold memory, symbolic graph/path algorithms, memory-augmented neural baselines. | A source-backed comparison table with exact claim boundary and closest-risk references. | Still missing as manuscript content; should be added only after final bibliography keys exist. |

## Candidate metadata for final bibliography work

These entries are candidates for the final bibliography and should be checked against the target venue style before insertion.

| Key | Candidate metadata |
|---|---|
| `McCloskeyCohen1989` | McCloskey, M. and Cohen, N. J. (1989). Catastrophic Interference in Connectionist Networks: The Sequential Learning Problem. *Psychology of Learning and Motivation*, 24, 109-165. DOI: `10.1016/S0079-7421(08)60536-8`. |
| `French1999` | French, R. M. (1999). Catastrophic forgetting in connectionist networks. *Trends in Cognitive Sciences*, 3(4), 128-135. DOI: `10.1016/S1364-6613(99)01294-2`. |
| `Kirkpatrick2017` | Kirkpatrick, J. et al. (2017). Overcoming catastrophic forgetting in neural networks. *Proceedings of the National Academy of Sciences*, 114(13), 3521-3526. DOI: `10.1073/pnas.1611835114`. |
| `Zenke2017` | Zenke, F., Poole, B., and Ganguli, S. (2017). Continual Learning Through Synaptic Intelligence. *Proceedings of Machine Learning Research*, 70, 3987-3995. |
| `Rebuffi2017` | Rebuffi, S.-A., Kolesnikov, A., Sperl, G., and Lampert, C. H. (2017). iCaRL: Incremental Classifier and Representation Learning. *CVPR 2017*. DOI: `10.1109/CVPR.2017.587`. |
| `LopezPaz2017` | Lopez-Paz, D. and Ranzato, M. (2017). Gradient Episodic Memory for Continual Learning. *NeurIPS 2017*. |
| `vanDeVenTolias2019` | van de Ven, G. M. and Tolias, A. S. (2019). Three scenarios for continual learning. arXiv: `1904.07734`. |
| `Graves2014` | Graves, A., Wayne, G., and Danihelka, I. (2014). Neural Turing Machines. arXiv: `1410.5401`. |
| `Graves2016` | Graves, A. et al. (2016). Hybrid computing using a neural network with dynamic external memory. *Nature*, 538, 471-476. DOI: `10.1038/nature20101`. |
| `Weston2014` | Weston, J., Chopra, S., and Bordes, A. (2014). Memory Networks. arXiv: `1410.3916`. |
| `Sukhbaatar2015` | Sukhbaatar, S., Weston, J., Fergus, R., et al. (2015). End-To-End Memory Networks. *NeurIPS 2015*. |
| `Santoro2016` | Santoro, A. et al. (2016). Meta-learning with memory-augmented neural networks. *Proceedings of Machine Learning Research*, 48, 1842-1850. |
| `Vinyals2016` | Vinyals, O. et al. (2016). Matching Networks for One Shot Learning. *NeurIPS 2016*. |
| `Hebb1949` | Hebb, D. O. (1949). *The Organization of Behavior: A Neuropsychological Theory*. New York: Wiley. |
| `Hopfield1982` | Hopfield, J. J. (1982). Neural networks and physical systems with emergent collective computational abilities. *PNAS*, 79(8), 2554-2558. DOI: `10.1073/pnas.79.8.2554`. |
| `HintonPlaut1987` | Hinton, G. E. and Plaut, D. C. (1987). Using fast weights to deblur old memories. *Proceedings of the Cognitive Science Society*, 9, 177-186. Final BibTeX verification still needed. |
| `Miconi2018` | Miconi, T., Clune, J., and Stanley, K. O. (2018). Differentiable plasticity: training plastic neural networks with backpropagation. *ICML 2018*. |
| `Miconi2019` | Miconi, T. et al. (2019). Backpropamine: training self-modifying neural networks with differentiable neuromodulated plasticity. *ICLR 2019*. |
| `Schlag2021FastWeights` | Schlag, I. et al. (2021). Linear Transformers Are Secretly Fast Weight Programmers. *Proceedings of Machine Learning Research*, 139, 9355-9366. |
| `Jacobs1991` | Jacobs, R. A., Jordan, M. I., Nowlan, S. J., and Hinton, G. E. (1991). Adaptive Mixtures of Local Experts. *Neural Computation*, 3(1), 79-87. DOI: `10.1162/neco.1991.3.1.79`. |
| `JordanJacobs1994` | Jordan, M. I. and Jacobs, R. A. (1994). Hierarchical Mixtures of Experts and the EM Algorithm. *Neural Computation*, 6(2), 181-214. DOI: `10.1162/neco.1994.6.2.181`. |
| `Rusu2016` | Rusu, A. A. et al. (2016). Progressive Neural Networks. arXiv: `1606.04671`. |
| `Fernando2017` | Fernando, C. et al. (2017). PathNet: Evolution Channels Gradient Descent in Super Neural Networks. *GECCO 2017*. |
| `Shazeer2017` | Shazeer, N. et al. (2017). Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer. arXiv: `1701.06538`; ICLR 2017. |
| `GershmanNiv2010` | Gershman, S. J. and Niv, Y. (2010). Learning latent structure: carving nature at its joints. *Current Opinion in Neurobiology*, 20(2), 251-256. DOI: `10.1016/j.conb.2010.02.008`. |
| `LakeBaroni2018` | Lake, B. M. and Baroni, M. (2018). Generalization without systematicity: On the compositional skills of sequence-to-sequence recurrent networks. *ICML 2018*. |
| `Hupkes2020` | Hupkes, D. et al. (2020). Compositionality Decomposed: How do Neural Networks Generalise? *Journal of Artificial Intelligence Research*. DOI: `10.1613/jair.1.11674`. |
| `Scarselli2009` | Scarselli, F. et al. (2009). The Graph Neural Network Model. *IEEE Transactions on Neural Networks*. DOI: `10.1109/TNN.2008.2005605`. |
| `Li2016` | Li, Y. et al. (2016). Gated Graph Sequence Neural Networks. *ICLR 2016*; arXiv: `1511.05493`. |
| `Battaglia2018` | Battaglia, P. W. et al. (2018). Relational inductive biases, deep learning, and graph networks. arXiv: `1806.01261`. |
| `Velickovic2020` | Velickovic, P. et al. (2020). Neural Execution of Graph Algorithms. *ICLR 2020*. |
| `OkeefeNadel1978` | O'Keefe, J. and Nadel, L. (1978). *The Hippocampus as a Cognitive Map*. Oxford: Oxford University Press. |
| `TeylerDiScenna1986` | Teyler, T. J. and DiScenna, P. (1986). The hippocampal memory indexing theory. *Behavioral Neuroscience*, 100(2), 147-154. DOI: `10.1037/0735-7044.100.2.147`. |
| `McClelland1995` | McClelland, J. L., McNaughton, B. L., and O'Reilly, R. C. (1995). Why there are complementary learning systems in the hippocampus and neocortex. *Psychological Review*, 102(3), 419-457. DOI: `10.1037/0033-295X.102.3.419`. |
| `NormanOReilly2003` | Norman, K. A. and O'Reilly, R. C. (2003). Modeling hippocampal and neocortical contributions to recognition memory. *Psychological Review*, 110(4), 611-646. DOI: `10.1037/0033-295X.110.4.611`. |
| `Eichenbaum2017` | Eichenbaum, H. (2017). On the Integration of Space, Time, and Memory. *Nature Reviews Neuroscience*. DOI: `10.1038/nrn.2017.74`. |
| `Kumaran2016` | Kumaran, D., Hassabis, D., and McClelland, J. L. (2016). What Learning Systems do Intelligent Agents Need? Complementary Learning Systems Theory Updated. *Trends in Cognitive Sciences*, 20(7), 512-534. DOI: `10.1016/j.tics.2016.05.004`. |

## Related-work wording risks

| Risk | Current issue | Required fix before submission |
|---|---|---|
| `modern transformer memory systems` | Section 2.2 mentions modern transformer memory systems, but the local placeholder list mostly covers external memory/memory-network precursors. | Either add specific transformer-memory/long-context/linear-attention references, or narrow the sentence to memory-augmented neural systems. |
| `task masks, adapters, parameter isolation` | Section 2.4 names several architectural families but currently cites only a small subset. | Add exact sources for task masks/adapters if those words remain, or narrow to progressive networks, PathNet, and MoE-style routing. |
| `closest prior-art risk table` | The manuscript asks for a table but the table is not yet written. | Add a source-backed table after final BibTeX keys exist. |
| `biological mechanism` | Neuroscience citations motivate indexing, CLS, and cognitive maps, but do not validate CIRM biologically. | Keep all biological statements as computational inspiration unless new evidence is added. |
| `broad neural comparison` | Exp15 is minimal fixed-profile; memory-augmented/key-value neural baselines are not present. | Keep C12 as discussion/table baseline posture unless the venue requires optional broader neural baselines. |

## Recommended next citation tasks

1. Create a venue-compatible bibliography file only after choosing the manuscript export path and citation style.
2. Replace manuscript placeholder keys with verified BibTeX keys.
3. Add a compact closest-prior-art table to Section 2.7.
4. Remove or narrow any related-work phrase whose cited source family is too broad.
5. Keep novelty framed as the controlled route-memory decomposition and evidence map, not as novelty of context gating, recurrence, replay, task isolation, modular routing, or memory augmentation in isolation.

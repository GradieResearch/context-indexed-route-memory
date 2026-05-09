# Manuscript References Ledger

Status: venue-neutral manuscript citation ledger; not a final journal-formatted bibliography.

Purpose: map the citation placeholders currently used in `docs/manuscript/draft/MANUSCRIPT_V2.md` to checked metadata so the final manuscript export can be converted to BibTeX, CSL JSON, numbered references, or author-year references without inventing citations.

Verification date: 2026-05-09.

## Conventions

- Keys match the placeholder keys already present in `MANUSCRIPT_V2.md`.
- Metadata was cross-checked against publisher, venue, indexing, author, or archival pages where available.
- This file deliberately does not choose a target journal style.
- This file deliberately does not broaden the manuscript claim posture. The references support background and boundary positioning; they do not establish broad CIRM-over-neural superiority, raw sensory latent-world discovery, biological validation, or solved continual learning.
- When page ranges differ across publisher proceedings views and DOI/proceedings indexes, the note records the ambiguity for final BibTeX export.

## Continual learning and catastrophic interference

| Key | Reference metadata | Identifier / note | Manuscript use |
|---|---|---|---|
| `McCloskeyCohen1989` | McCloskey, M. and Cohen, N. J. (1989). Catastrophic Interference in Connectionist Networks: The Sequential Learning Problem. *Psychology of Learning and Motivation*, 24, 109-165. | DOI: `10.1016/S0079-7421(08)60536-8`. | Classic catastrophic interference framing. |
| `French1999` | French, R. M. (1999). Catastrophic forgetting in connectionist networks. *Trends in Cognitive Sciences*, 3(4), 128-135. | DOI: `10.1016/S1364-6613(99)01294-2`. | Catastrophic forgetting overview. |
| `Kirkpatrick2017` | Kirkpatrick, J. et al. (2017). Overcoming catastrophic forgetting in neural networks. *Proceedings of the National Academy of Sciences*, 114(13), 3521-3526. | DOI: `10.1073/pnas.1611835114`. | Regularization-based continual-learning example. |
| `Zenke2017` | Zenke, F., Poole, B., and Ganguli, S. (2017). Continual Learning Through Synaptic Intelligence. *Proceedings of Machine Learning Research*, 70, 3987-3995. | ICML/PMLR. | Synaptic intelligence / regularization family. |
| `Rebuffi2017` | Rebuffi, S.-A., Kolesnikov, A., Sperl, G., and Lampert, C. H. (2017). iCaRL: Incremental Classifier and Representation Learning. *CVPR 2017*. | DOI: `10.1109/CVPR.2017.587`. Final page range should use the target bibliography export because publisher/proceedings views differ. | Class-incremental exemplar-memory baseline family. |
| `LopezPaz2017` | Lopez-Paz, D. and Ranzato, M. (2017). Gradient Episodic Memory for Continual Learning. *NeurIPS 2017*. | NeurIPS proceedings. | Episodic-memory/replay constraint family. |
| `vanDeVenTolias2019` | van de Ven, G. M. and Tolias, A. S. (2019). Three scenarios for continual learning. arXiv:1904.07734. | arXiv: `1904.07734`. | Continual-learning scenario taxonomy. |

## Memory-augmented computation and few-shot memory

| Key | Reference metadata | Identifier / note | Manuscript use |
|---|---|---|---|
| `Graves2014` | Graves, A., Wayne, G., and Danihelka, I. (2014). Neural Turing Machines. arXiv:1410.5401. | arXiv: `1410.5401`. | Differentiable external-memory background. |
| `Graves2016` | Graves, A. et al. (2016). Hybrid computing using a neural network with dynamic external memory. *Nature*, 538, 471-476. | DOI: `10.1038/nature20101`. | Differentiable Neural Computer / dynamic external memory. |
| `Weston2014` | Weston, J., Chopra, S., and Bordes, A. (2014). Memory Networks. arXiv:1410.3916. | arXiv: `1410.3916`. | Memory-network background. |
| `Sukhbaatar2015` | Sukhbaatar, S., Weston, J., Fergus, R., et al. (2015). End-To-End Memory Networks. *NeurIPS 2015*. | NeurIPS proceedings. | End-to-end memory-network background. |
| `Santoro2016` | Santoro, A. et al. (2016). Meta-learning with memory-augmented neural networks. *Proceedings of Machine Learning Research*, 48, 1842-1850. | ICML/PMLR. | Memory-augmented meta-learning background. |
| `Vinyals2016` | Vinyals, O. et al. (2016). Matching Networks for One Shot Learning. *NeurIPS 2016*. | NeurIPS proceedings. | Attention/memory-based one-shot learning background. |

## Fast weights, associative memory, and differentiable plasticity

| Key | Reference metadata | Identifier / note | Manuscript use |
|---|---|---|---|
| `Hebb1949` | Hebb, D. O. (1949). *The Organization of Behavior: A Neuropsychological Theory*. New York: Wiley. | Book; no DOI expected. | Hebbian/plasticity motivation only. |
| `Hopfield1982` | Hopfield, J. J. (1982). Neural networks and physical systems with emergent collective computational abilities. *Proceedings of the National Academy of Sciences*, 79(8), 2554-2558. | DOI: `10.1073/pnas.79.8.2554`. | Associative memory background. |
| `HintonPlaut1987` | Hinton, G. E. and Plaut, D. C. (1987). Using fast weights to deblur old memories. *Proceedings of the Ninth Annual Conference of the Cognitive Science Society*, 177-186. | Final publisher field should be normalized during BibTeX export. | Fast-weight background. |
| `Miconi2018` | Miconi, T., Clune, J., and Stanley, K. O. (2018). Differentiable plasticity: training plastic neural networks with backpropagation. *Proceedings of Machine Learning Research*, 80. | ICML/PMLR. Final page range should use the PMLR export. | Differentiable-plasticity background. |
| `Miconi2019` | Miconi, T. et al. (2019). Backpropamine: training self-modifying neural networks with differentiable neuromodulated plasticity. *ICLR 2019*. | ICLR proceedings. | Neuromodulated differentiable plasticity background. |
| `Schlag2021FastWeights` | Schlag, I. et al. (2021). Linear Transformers Are Secretly Fast Weight Programmers. *Proceedings of Machine Learning Research*, 139, 9355-9366. | ICML/PMLR. | Fast-weight / linear-attention relation. |

## Context, gating, modularity, and latent task inference

| Key | Reference metadata | Identifier / note | Manuscript use |
|---|---|---|---|
| `Jacobs1991` | Jacobs, R. A., Jordan, M. I., Nowlan, S. J., and Hinton, G. E. (1991). Adaptive Mixtures of Local Experts. *Neural Computation*, 3(1), 79-87. | DOI: `10.1162/neco.1991.3.1.79`. | Mixture-of-experts / gating prior art. |
| `JordanJacobs1994` | Jordan, M. I. and Jacobs, R. A. (1994). Hierarchical Mixtures of Experts and the EM Algorithm. *Neural Computation*, 6(2), 181-214. | DOI: `10.1162/neco.1994.6.2.181`. | Hierarchical mixture-of-experts prior art. |
| `Rusu2016` | Rusu, A. A. et al. (2016). Progressive Neural Networks. arXiv:1606.04671. | arXiv: `1606.04671`. | Architectural expansion / parameter isolation background. |
| `Fernando2017` | Fernando, C. et al. (2017). PathNet: Evolution Channels Gradient Descent in Super Neural Networks. *GECCO 2017*. | arXiv: `1701.08734`. | Path/module selection background. |
| `Shazeer2017` | Shazeer, N. et al. (2017). Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer. *ICLR 2017*. | arXiv: `1701.06538`. | Sparse routing / large-scale MoE prior art. |
| `GershmanNiv2010` | Gershman, S. J. and Niv, Y. (2010). Learning latent structure: carving nature at its joints. *Current Opinion in Neurobiology*, 20(2), 251-256. | DOI: `10.1016/j.conb.2010.02.008`. | Latent-cause/context inference background. |

## Compositional generalization, graph reasoning, and neural algorithmic reasoning

| Key | Reference metadata | Identifier / note | Manuscript use |
|---|---|---|---|
| `LakeBaroni2018` | Lake, B. M. and Baroni, M. (2018). Generalization without systematicity: On the compositional skills of sequence-to-sequence recurrent networks. *ICML 2018*. | ICML/PMLR. | Compositional-generalization background. |
| `Hupkes2020` | Hupkes, D. et al. (2020). Compositionality Decomposed: How do Neural Networks Generalise? *Journal of Artificial Intelligence Research*, 67, 757-795. | DOI: `10.1613/jair.1.11674`. | Compositional-generalization taxonomy/background. |
| `Scarselli2009` | Scarselli, F. et al. (2009). The Graph Neural Network Model. *IEEE Transactions on Neural Networks*, 20(1), 61-80. | DOI: `10.1109/TNN.2008.2005605`. | Graph neural-network background. |
| `Li2016` | Li, Y. et al. (2016). Gated Graph Sequence Neural Networks. *ICLR 2016*. | arXiv: `1511.05493`. | Gated graph sequence model background. |
| `Battaglia2018` | Battaglia, P. W. et al. (2018). Relational inductive biases, deep learning, and graph networks. arXiv:1806.01261. | arXiv: `1806.01261`. | Graph-network / relational-inductive-bias background. |
| `Velickovic2020` | Velickovic, P. et al. (2020). Neural Execution of Graph Algorithms. *ICLR 2020*. | ICLR proceedings. | Neural algorithmic reasoning background. |

## Hippocampal indexing, cognitive maps, and complementary learning systems

| Key | Reference metadata | Identifier / note | Manuscript use |
|---|---|---|---|
| `OkeefeNadel1978` | O'Keefe, J. and Nadel, L. (1978). *The Hippocampus as a Cognitive Map*. Oxford: Oxford University Press. | Book; no DOI expected. | Cognitive-map inspiration only. |
| `TeylerDiScenna1986` | Teyler, T. J. and DiScenna, P. (1986). The hippocampal memory indexing theory. *Behavioral Neuroscience*, 100(2), 147-154. | DOI: `10.1037/0735-7044.100.2.147`. | Hippocampal indexing inspiration only. |
| `McClelland1995` | McClelland, J. L., McNaughton, B. L., and O'Reilly, R. C. (1995). Why there are complementary learning systems in the hippocampus and neocortex. *Psychological Review*, 102(3), 419-457. | DOI: `10.1037/0033-295X.102.3.419`. | CLS/stability-plasticity motivation only. |
| `NormanOReilly2003` | Norman, K. A. and O'Reilly, R. C. (2003). Modeling hippocampal and neocortical contributions to recognition memory. *Psychological Review*, 110(4), 611-646. | DOI: `10.1037/0033-295X.110.4.611`. | Hippocampal/neocortical modeling inspiration only. |
| `Eichenbaum2017` | Eichenbaum, H. (2017). On the Integration of Space, Time, and Memory. *Neuron*, 95(5), 1007-1018. | DOI: `10.1016/j.neuron.2017.06.036`. Corrects the earlier audit mismatch that paired this title with a Nature Reviews Neuroscience DOI for a different Eichenbaum paper. | Space/time/memory organization inspiration only. |
| `Kumaran2016` | Kumaran, D., Hassabis, D., and McClelland, J. L. (2016). What Learning Systems do Intelligent Agents Need? Complementary Learning Systems Theory Updated. *Trends in Cognitive Sciences*, 20(7), 512-534. | DOI: `10.1016/j.tics.2016.05.004`. | Updated CLS framing and AI relevance, motivation only. |

## Citation insertion notes

- `MANUSCRIPT_V2.md` currently uses bracketed placeholder keys rather than a chosen venue citation style. These keys now have a local metadata ledger in this file.
- The phrase `modern transformer memory systems` in Section 2.2 should either be narrowed to memory-augmented neural systems covered by the current keys or expanded with exact transformer-memory/long-context references in a later pass.
- The phrase `task masks, adapters, parameter isolation` in Section 2.4 should either be narrowed to the currently cited families or expanded with exact task-mask/adapter references in a later pass.
- Biological citations should remain motivational. They do not validate CIRM as a biological mechanism.
- Neural comparator citations should remain background and limitation framing. Exp15 is a minimal fixed-profile comparator, not exhaustive neural benchmarking.

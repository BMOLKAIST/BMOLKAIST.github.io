---
layout: page
title: research
permalink: /research/
description: Optics and AI to understand, diagnose, and treat human disease — and to measure the systems that industry builds.
nav: true
nav_order: 3
toc:
  sidebar: left
---

<!-- pages/projects.md — single scrolling research page. The sidebar table of contents
     is generated automatically by al-folio from the ## headings below (toc.sidebar). -->

The Biomedical Optics Laboratory develops optical methods to measure and shape light for quantitative, label-free, and non-destructive insight into complex systems — and, increasingly, pairs light with complementary probes such as X-ray and ultrasound. From this single foundation in measurement science, our work reaches across two frontiers. In human health — the lab's founding commitment and the larger share of what we do — we image living cells, tissues, and embryos to understand, diagnose, and help treat disease. In advanced industry, the same physics addresses semiconductor and display metrology and inspection. Across both frontiers, we increasingly couple these measurements with machine learning to move from images to decisions.

Our research is organized into four areas — imaging methods for life science, metrology and inspection methods for industry, biological and medical applications, and in vitro fertilization — each drawing on the others. We welcome students, collaborators, and partners who want to measure what has been hard to see, and to help decide what to do with it.

---

## Label-Free 3D Imaging of Living Matter

Quantitative phase imaging and holotomography that resolve the three-dimensional architecture of living cells without stains, dyes, or fixation — and that we are pushing toward thicker, more scattering specimens.

*Established: label-free 3D refractive-index imaging of living cells. Building toward: greater depth, speed, and fidelity in thicker samples.*

**What it is.** This is the lab's foundation: the optical and computational methods that let us measure how living matter bends light, and turn that measurement into quantitative three-dimensional structure. We develop quantitative phase imaging (QPI) and holotomography (HT) — and modalities that extend beyond them — by co-designing the interferometric hardware, the illumination scheme, and the reconstruction algorithm as a single system rather than treating imaging and inversion separately. Because the contrast comes from a sample's own refractive index, the same measurement yields a physically meaningful map — local dry mass, morphology, and dynamics — with no exogenous label to perturb the cell. Much of the lab's work in biology, medicine, and industry builds on the imaging methods developed here.

**Why it matters.** Fluorescence and histological staining, for all their molecular specificity, alter the sample, photobleach over time, and rarely give absolute quantities. Label-free 3D refractive-index imaging offers a complementary path: it is quantitative, non-destructive, and gentle enough to follow the same live cell over hours to days, which makes it well suited to longitudinal studies, standardized measurement, and settings where fixation or labeling is impractical. Strengthening these methods — improving resolution, imaging depth, speed, and reconstruction fidelity — raises the ceiling for the applications built on them, from single-cell biophysics to clinical and industrial imaging.

**Representative directions.**

- **New QPI and holotomography modalities** — Interferometric and illumination-engineered optical systems, beyond conventional QPI and HT, that improve spatial resolution, acquisition speed, field of view, and robustness, so that live-cell 3D refractive-index imaging becomes faster and more accessible.
- **Refractive-index tomography and inverse-scattering reconstruction** — Reconstruction algorithms that convert measured light fields into 3D refractive-index maps, including models that account for multiple scattering and the missing-cone problem, providing a path toward more accurate tomography of optically thicker specimens.
- **Imaging deeper into scattering samples and tissues** — Extending label-free measurement from isolated cells toward organoids, spheroids, and tissue-scale samples, where multiply scattered light degrades contrast — combining optical design with computational correction to recover structure at greater depth.
- **Quantitative biophysical readouts from refractive index** — Turning the measured refractive index into calibrated biophysical quantities — local dry-mass density, cell and organelle morphology, and their temporal dynamics — as standardized, label-free descriptors of living cells.

**Representative publications.**

{% bibliography --query @*[key=lee2026incoherent || key=kim2024holotomography || key=oh2025extending] %}

*For prospective students:* here you would build imaging instruments and reconstruction algorithms end to end — optics, illumination, and computation as one system. If that combination appeals to you, we would be glad to hear from you.

---

## Seeing Inside What Manufacturing Builds

The same light-field measurement approach that images living cells without staining, turned toward the buried interfaces and transparent structures of advanced manufacturing.

*Established: quantitative, label-free optical and X-ray measurement of transparent and layered structures. Building toward: fusing optics, X-ray, and ultrasound into a single registered volume for buried interfaces.*

**What it is.** The physics we developed to see inside a living cell without staining it — recovering the full complex light field, reconstructing three-dimensional refractive-index structure, and shaping wavefronts through scattering media — is fundamentally a set of tools for non-destructive, quantitative measurement of things that are hard to see. In this area we carry that toolkit into semiconductor and display manufacturing, where the features of interest are increasingly transparent (glass, dielectrics), buried (bonded interfaces, stacked dies), or below the reach of any single modality. Our approach treats optics together with complementary probes — X-ray and ultrasound — not as competing techniques but as different views of the same volume, unified by a common computational-imaging and inverse-problem framework. The goal is measurement that is quantitative, traceable, and gentle on the sample rather than destructive cross-sectioning.

**Why it matters.** Advanced packaging and display fabrication are moving toward architectures — through-glass vias, hybrid bonding, heterogeneous 3D integration, microLED arrays — where the critical features sit inside a stack and are optically or physically inaccessible to conventional surface metrology. Yield at these nodes depends on catching small voids, misalignment, and interface defects without sacrificing the part. A measurement discipline built around penetrating, label-free, quantitative imaging may enable in-line inspection where today's practice still relies on sampling and destructive analysis, providing a path toward tighter process control at manufacturing scale.

**Representative directions.**

- **Non-destructive volumetric metrology of transparent and layered structures** — Phase- and refractive-index-based tomography adapted from holotomography to characterize glass substrates, through-glass vias, and dielectric stacks in three dimensions. Because transparent materials are exactly where amplitude-only imaging fails, quantitative phase measurement offers a natural probe of crack, void, and taper geometry without cross-sectioning.
- **Multimodal fusion for buried interfaces** — Different probes access different opacity and depth regimes: optics for transparent and near-surface layers, X-ray for high-density and deeply buried features, ultrasound for acoustic-impedance contrast at bonded interfaces. We are developing joint reconstruction that fuses these into a single registered volume, targeting hybrid-bonding voids and stacked-die alignment that no single method resolves alone.
- **Computational and learning-based inverse methods for inspection** — Physics-informed reconstruction and machine learning transferred from our biological imaging work — recovering structure from indirect, noisy, or partial measurements. Applied to inspection, this could support defect classification and virtual metrology, inferring hard-to-measure parameters from faster, cheaper signals.
- **Quantitative characterization for display and emitter metrology** — Extending quantitative optical measurement to OLED and microLED devices — uniformity, layer structure, and defect signatures — where label-free, non-contact readout may complement electrical and photometric testing during panel and array fabrication.

**Representative publications.** *(Optical and X-ray metrology methods underpinning this direction; semiconductor- and display-specific inspection studies are in active development.)*

{% bibliography --query @*[key=jo2024three || key=lee2024visualizing || key=lee2026speckle] %}

*For prospective students:* this area is where optical physics meets real manufacturing constraints. You would adapt imaging and inverse-problem methods to industrially relevant samples and work at the interface between the lab and the systems that industry builds.

---

## Observing Living Biology as It Unfolds

Label-free 3D imaging and AI, brought together to ask harder questions in organoid, cancer, developmental, and regenerative biology.

*Established: non-destructive, longitudinal imaging of living, unstained specimens. Building toward: learned models that turn 3D volumes into interpretable, quantitative biology.*

**What it is.** This area applies the lab's quantitative, label-free 3D imaging methods — coupled with machine learning — to biological systems that resist conventional approaches: organoids, three-dimensional cancer models, developing embryos, and engineered tissues for regenerative medicine. Because holotomographic imaging measures refractive index directly, it can follow living, unstained specimens over hours to days without the phototoxicity and labeling constraints that limit fluorescence. Our strategy is to pair that continuous, quantitative readout with learned models that turn raw 3D volumes into interpretable biology — morphodynamic trajectories, virtual molecular stains, and phenotypic profiles. The aim is not imaging for its own sake, but measurement-driven methods that let biologists observe processes as they unfold rather than infer them from fixed endpoints.

**Why it matters.** Much of modern biology is studied in destructive snapshots: cells are fixed, stained, or dissociated, and dynamics are inferred from populations rather than observed in individuals. Label-free 3D imaging combined with AI offers a complementary path — non-destructive, longitudinal observation of the same living specimen, quantified volume by volume. For organoid and 3D cancer models this may improve reproducibility and open access to growth, differentiation, and drug-response trajectories that endpoint assays miss; for developmental biology it could enable gentle, continuous observation of morphogenesis; and for regenerative medicine it provides a route toward standardized, quantitative quality assessment of living cell and tissue products.

**Representative directions.**

- **Longitudinal live imaging of unlabeled organoids** — Following the same organoid non-destructively over its full culture course to quantify growth, budding, and differentiation. Label-free 3D imaging avoids the phototoxicity and marker constraints of repeated fluorescence, providing a path toward more reproducible, quantitative organoid assays and drug-response readouts.
- **Morphodynamics of 3D cancer and developmental systems** — Learning the temporal grammar of how tumor spheroids, invading cells, and developing embryos change shape and internal organization over time. Continuous 3D refractive-index measurements feed models that extract migration, division, and morphogenetic trajectories as dynamics rather than fixed endpoints.
- **AI virtual staining of live 3D specimens** — Training models to infer molecular and histological contrast — nuclei, organelles, tissue-like stains — directly from label-free volumes. This could complement conventional staining by suggesting where and what to label, while preserving the specimen for continued live observation.
- **Phenotypic profiling and quality assessment for regenerative medicine** — Building quantitative, label-free phenotypic signatures of cells and engineered tissues to support cell-therapy and regenerative-medicine workflows. High-content 3D profiling provides a non-destructive path toward standardized characterization and release-quality assessment of living products.

**Representative publications.**

{% bibliography --query @*[key=park2025revealing || key=lee2024long || key=oh2026morphology] %}

*For prospective students:* if you are drawn to biological questions and want to work where quantitative imaging and machine learning meet live-cell biology, this is where our methods meet real specimens and collaborators.

---

## Non-Invasive Imaging for Assisted Reproduction

Label-free imaging and AI for non-invasive assessment and selection of oocytes, sperm, and embryos.

*Established: stain-free, quantitative imaging of individual gametes. Building toward: quantitative, AI-based selection readouts validated for clinical embryology.*

**What it is.** Clinical embryology still depends heavily on subjective, morphology-based grading of gametes and embryos under conventional microscopy, and the most informative molecular assays are destructive — unacceptable for cells intended for transfer. We develop label-free, quantitative imaging methods, grounded in the lab's work on quantitative phase imaging and holotomography, that aim to measure the intrinsic optical properties of living oocytes, sperm, and embryos without dyes, fixation, or genetic reporters. Because these measurements are non-invasive and quantitative, they can be repeated over time on the same specimen and coupled with AI models that learn objective, reproducible signatures of developmental competence. The aim is to move embryo and gamete selection from expert visual judgment toward measurement-driven, auditable decisions that a clinic can standardize across operators and sites.

**Why it matters.** Embryo and gamete selection is a high-leverage and, today, only weakly standardized step in assisted reproduction: the choice of which embryo to transfer strongly shapes success rates, yet current grading is operator-dependent and hard to reproduce between clinics. A method that is simultaneously non-invasive — so it carries no added risk to a specimen destined for transfer — and quantitative could provide a path toward more consistent, evidence-based selection, could reduce reliance on invasive genetic testing, and could make outcomes more comparable across laboratories. This is a clinically consequential, directly translational problem where label-free optics and AI are well matched to the constraint that the specimen must remain viable.

**Representative directions.**

- **Label-free oocyte quality assessment** — Quantitative phase and 3D refractive-index imaging of living oocytes to derive objective descriptors of cytoplasmic and structural organization, as a non-invasive complement to visual grading for identifying oocytes with higher developmental potential.
- **Sperm morphology and motility analysis** — Stain-free imaging of individual sperm to quantify head and midpiece morphology together with motility dynamics, supporting more objective selection criteria than manual assessment while avoiding stains that could compromise cells used for fertilization.
- **Non-invasive embryo scoring for transfer** — Time-resolved, label-free imaging of preimplantation embryos combined with AI models that learn quantitative signatures of developmental competence, toward embryo ranking that could complement, and potentially reduce reliance on, invasive biopsy-based testing.
- **AI-based selection models with reproducible readouts** — Machine-learning pipelines trained on quantitative label-free measurements rather than qualitative images, aimed at operator-independent, auditable selection scores that may enable standardization of embryology decisions across clinics.

**Representative publications.**

{% bibliography --query @*[key=kim2026holotomography] %}

*Embryo, blastocyst, and sperm assessment studies from the lab are in preparation and will be added on publication.*

*For prospective students:* this area sits directly at the clinic-facing edge of the lab — imaging physics and AI applied to a problem where non-invasiveness is a hard constraint and clinical impact is immediate.

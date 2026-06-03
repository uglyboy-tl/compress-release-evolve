# Compression, Release, and Evolution: A Unified Systems Theory from Entropy

> **Authors**: [Author Name]
> **Date**: 2026-05-25 (first published) / 2026-06-02 (white paper)
> **Status**: Concept paper / White paper
> **License**: CC BY-NC-SA 4.0

---

## Abstract

Systems across physics, biology, and society exhibit a shared structural pattern: local order is maintained by transferring randomness to other dimensions, and long-term survival depends on balancing control with strategic flexibility. Here we propose a unified systems theory built on a single axiom — **entropy = randomness** — that derives the mechanisms of control, antifragility, and evolution from first principles. We define control as **compression mapping** (f: X → Y, where |Y| < |X|), which transfers entropy across dimensions without reducing total entropy. From this foundation, we derive rigidity and flexibility as poles on a control-intensity spectrum, and antifragility as the system-level balance between the two. We further propose that evolution follows a positive-feedback cycle of **entropy decrease (new codes) → entropy increase (new combinations) → new entropy decrease**, which is driven by life's foundational property of actively feeding on entropy. We apply this framework to diagnose three structural fallacies — **coding reversal, dimension compression bias, and self-referential closure** — shared across eight disciplines: economics, natural science, political science, law, medicine, education, artificial intelligence, and management. The theory provides a unified diagnostic language for identifying when control is applied to the wrong dimensions, and offers a direction for building systems that maintain evolutionary capacity under unanticipated shocks. The framework is currently qualitative; formalization and empirical validation are proposed as next steps.

---

## 1. Introduction

The second law of thermodynamics states that total entropy in an isolated system never decreases. Yet every day we observe systems becoming more ordered: organisms grow, technologies iterate, and civilizations accumulate complexity. This apparent contradiction between the thermodynamic arrow and the arrow of complexification has been a central puzzle in science since Boltzmann.

Existing resolutions fall into two broad categories. One tradition, exemplified by Prigogine's dissipative structures (Prigogine & Stengers, 1984) and Schrödinger's "negative entropy" (Schrödinger, 1944), explains order as the product of open systems that export entropy to their environment. Another tradition, represented by Holling's adaptive cycle and panarchy framework (Holling, 1973; Gunderson & Holling, 2002), describes how complex systems cycle through phases of growth, conservation, release, and reorganization. Both traditions capture essential aspects of the puzzle, but neither provides a unified mechanism that connects the thermodynamic roots of order to the observable failure modes of real-world systems across disciplines.

This paper proposes a unified systems theory that starts from a single axiom — **entropy = randomness** — and derives the full chain of control, antifragility, and evolution through a series of definitions and deductions. The theory's core move is to define **control as compression mapping**: the operation of reducing the number of possible states in a target dimension. This definition immediately yields a non-trivial consequence: total entropy never decreases, it only transfers from one dimension to another. Control is not the elimination of disorder — it is the transportation of entropy.

From this mechanism, we derive a diagnostic framework for analyzing why systems fail. We identify three cross-disciplinary fallacy patterns and apply them to eight disciplines. We conclude by proposing antifragility — defined as the balance between rigidity (control intensity) and flexibility (strategy space) — as a cross-disciplinary meta-standard for evaluating theories, policies, and institutional designs.

**Key difference from traditional science:** Traditional science asks "Given initial conditions, what happens?" (state derivation). This theory asks "Given the current control distribution, which dimensions are being hollowed out by invisible entropy leakage under random shocks?" (risk assessment). The two questions are complementary: state derivation excels in domains where control is deep and entropy leakage is minimal (e.g., particle physics); risk assessment becomes necessary where control is shallow and leakage is high (e.g., social systems, organizational design).

---

## 2. Theoretical Framework

### 2.1 Entropy

We define entropy as **randomness** — the number of distinct states a system can occupy. This definition is consistent with the thermodynamic definition (S = k ln W, where W is the number of microstates) and the information-theoretic definition (H = -Σ p_i ln p_i). In both cases, entropy quantifies the size of the possibility space.

A room with books scattered across the floor, glasses on random surfaces, and cables tangled in arbitrary configurations has high entropy — the number of possible arrangements is combinatorially large. The same room after tidying, with every object in a designated position, has low entropy in the object-position dimension — only one or a few arrangements correspond to "tidy."

### 2.2 Control as Compression Mapping

Control, in this framework, is defined as the operation of reducing randomness in a specific dimension. The mechanism that implements control is a **compression mapping**:

**f: X → Y, where |Y| < |X|**

Multiple states in the input space X are mapped to the same state in the output space Y. For example, when a team is told to "use Python for the backend," the programming-language dimension is compressed from dozens of possible languages to one. When a recipe specifies "use only three seasonings," the seasoning dimension is compressed from a large combinatorial space to a small one.

**The key consequence** is that total entropy does not decrease. The entropy "removed" from the compressed dimension does not vanish — it leaks into dimensions not covered by the compression mapping. When you compress the seasoning dimension, you must now innovate more intensely in cooking technique, heat control, and ingredient pairing to compensate. The total complexity of cooking has not decreased; it has merely redistributed.

This principle is isomorphic to the second law of thermodynamics: no process reduces total entropy. What appears to be entropy reduction in a focal dimension is always accompanied by entropy increase in other dimensions. **Control is entropy transportation, not entropy elimination.**

### 2.3 Rigidity and Flexibility

With compression mapping as the mechanism of control, we can define two poles on a continuous spectrum of control intensity:

**Rigidity** = more control. A rigid system applies compression mapping to more dimensions, or applies tighter constraints within a given dimension. The total control quantity is larger, and the remaining strategy space — the set of alternative paths the system can take — is narrower. A glass bowl is an extreme case: almost every molecule is locked into a crystal lattice, leaving virtually no strategy space. When dropped, the bowl has exactly one path: fracture along crystal planes.

**Flexibility** = less control. A flexible system applies fewer compression mappings, or applies looser constraints. The total control quantity is smaller, and the remaining strategy space is wider. A sponge is flexible: it can deform, bounce, and absorb impact because its structure leaves room for molecular rearrangement.

Rigidity and flexibility are **neutral descriptive terms**, not normative labels. Neither is inherently good or bad. A system is "too rigid" when its strategy space is so narrow that it cannot respond to events falling outside its compressed pathways. A system is "too flexible" when its control is too weak to maintain coherent structure — it ceases to be a system at all and becomes random drift.

### 2.4 Antifragility

We define **antifragility** as a qualitative indicator of how much randomness a system can handle in the dimensions it controls. It is not a precise scalar quantity — two different dimensions' "randomness-handling capacity" cannot be directly compared. Rather, antifragility provides a direction for reasoning: before any decision, ask "Does this increase the system's overall antifragility?" rather than "Does this make a specific metric more efficient?"

Antifragility requires a balance between rigidity and flexibility:

- **Too rigid** → strategy space is too narrow → the system collapses when a random event falls outside its narrow path. Examples: cancer cells (all control compressed into the division dimension, causing host death); glass bowls (zero strategy space for handling impact).
- **Too flexible** → control is too weak → the system cannot maintain coherent structure. Example: a team with no task allocation, no quality standards, and no coordination mechanism — each member has maximum freedom, but the system as a whole has collapsed.

The critical insight is that **antifragility is defined on the system as a whole, not on individual controls.** A system can have multiple controls operating simultaneously, but if they counteract each other without forming a coherent force, antifragility does not increase. The art of system design is not maximizing control — it is drawing the correct **dimension distribution map**: which dimensions need control, and which dimensions need room to breathe.

**Common misconceptions corrected:**

1. **Rigidity ≠ antifragility.** More control narrows strategy space. A stone is extremely rigid but shatters on impact.
2. **Flexibility ≠ antifragility.** Removing all control from a team increases freedom but destroys coordination. Antifragility requires both legs: control force and strategy space.
3. **Speed + pressure ≠ optimal.** Acceleration increases entropy production; increasing control simultaneously narrows the dissipation channels. The result is internal entropy accumulation and eventual burnout — analogous to placing an air conditioner's outdoor unit inside the room.

### 2.5 System, Subsystem, and Heat Dissipation

A **system** is a set of elements operating under shared control, forming a coherent whole. A system is not a static object but a continuous process of control maintenance. A band is not "four people with instruments" — it is those four people continuously playing according to a shared score. When the playing stops, the system ceases to exist.

Every system must release entropy to its environment. Maintaining low entropy in certain dimensions (order) necessarily produces high entropy in other dimensions. If the entropy production rate exceeds the **heat dissipation bandwidth** — the capacity of available dimensions to absorb and release entropy — the system accumulates entropy internally until it collapses. A system that runs faster produces more entropy and requires more dissipation bandwidth. Speed without bandwidth expansion makes a system more fragile, not stronger.

A **subsystem** exists within a parent system. In some dimensions, the subsystem maintains low entropy not through its own control but because the parent system provides it. A cell in the human body does not need to maintain its own temperature — the body does it. This is also the subsystem's vulnerability: if the parent system fails, the subsystem collapses in those dimensions.

### 2.6 Life: Feeding on Entropy

Schrödinger famously described life as feeding on "negative entropy" — absorbing order from the environment to maintain internal order (Schrödinger, 1944). We propose a crucial inversion: **life does not resist entropy; it actively seeks it.** Life feeds on entropy — it actively searches for randomness in specific dimensions (novel information, external stimuli, environmental energy), ingests it, metabolizes it, and expels the waste. In the process, it maintains low entropy in its critical dimensions.

This inversion resolves a puzzle: why does seeking novelty feel good? Evolution embedded dopamine reward mechanisms that make entropy-seeking behavior pleasurable. Scrolling through social media for new content, exploring unfamiliar terrain, learning a new skill — these are not failures of self-control but manifestations of life's foundational engine. The pleasure of finding new randomness drives the continued ingestion of entropy, which drives the evolutionary cycle forward. Life is not a defender against entropy; it is a predator of entropy.

### 2.7 Coding and Coding Evolution

**Coding** is the expression of a system's control rules. An organization's regulations, a programming language's syntax, a species' genome — these are all codes. By describing systems through codes, we can study system evolution as code evolution.

**Coding evolution** follows a positive-feedback cycle:

> **Entropy decrease (new codes) → Entropy increase (new-old combinations) → New entropy decrease → ...**

- **First half-beat: Entropy decrease.** A new code is formed — a new constraint that reduces randomness in a specific dimension of expression. The Tang Dynasty's regulated verse (jueju) imposed strict syllabic and tonal constraints on poetry — a compression mapping on the dimension of linguistic expression.
- **Second half-beat: Entropy increase.** The new code combines with existing codes, generating an explosion of new combinatorial possibilities. The constraints of regulated verse, rather than killing poetry, forced poets to explore imagery, inversion, and word-crafting dimensions that everyday language never needed. The information density of regulated verse far exceeds that of ordinary speech.
- **Cycle repeats.** The new combinatorial richness eventually exposes new dimensions that need control, prompting the formation of yet newer codes. Song Dynasty ci poetry loosened some constraints; modern free verse loosened others. Each relaxation is a new round of entropy increase on the combinatorial dimension, followed by new constraints.

This cycle operates without requiring a conscious "coder." Gravity spontaneously compresses matter into galactic disks — a compression mapping without a designer. Human-designed codes (laws, programming languages) and spontaneously emerged codes (physical laws, market conventions) are both valid instances of the same mechanism.

**Why evolution never stops:** Every round of entropy decrease (gaining control) necessarily produces more entropy in the code-usage dimension. More entropy means more randomness, which creates new control demands. This is a positive feedback loop. There is no terminal state of "perfect control" — the combinatorial space of code interactions is factorial in the number of codes, far exceeding any control system's capacity to cover.

### 2.8 Evolution as a System

The process of evolution itself can be analyzed as a system, with its own control mechanisms, strategy space, and antifragility:

- **Natural selection** is the rigid face of the evolutionary system — a compression mapping that eliminates unfit individuals, converging the population toward adaptive states.
- **Genetic drift (random variation)** is the flexible face — small-scale random perturbations that explore adjacent possibilities in the state space.
- **Recombination** (genetic recombination, code recombination) operates at the code level — splicing code fragments from different sources to produce new combinations, which are then filtered by selection.

A healthy evolutionary system requires balance between these forces: excessive drift → convergence too slow (too flexible); excessive selection pressure → diversity flattened (too rigid); rich recombination with moderate selection → both strategy space and filtering efficiency.

Evolution also evolves its own mechanisms. The transition from asexual to sexual reproduction, from purely genetic transmission to cultural transmission (language), and from waiting for real mutations to counterfactual reasoning (imagining "what if" scenarios) — each represents a meta-level compression mapping on the "means of evolution" dimension itself, creating new layers of control that dramatically accelerate the evolutionary cycle.

---

## 3. Relation to Existing Theories

The proposed framework integrates and extends several established intellectual traditions while introducing novel elements.

### 3.1 Thermodynamics and Information Theory

The theory's definition of entropy as randomness is consistent with both thermodynamic entropy (Boltzmann, 1877; Gibbs, 1878) and information-theoretic entropy (Shannon, 1948). The mathematical structure — a functional that is additive, convex, and positive-definite, measuring the size of a possibility space — is shared across all three. The theory extends this structure to the analysis of social, organizational, and institutional systems, where the "possibility space" is the set of behaviors, strategies, or states available to agents.

### 3.2 Cybernetics and Control Theory

Ashby's Law of Requisite Variety (Ashby, 1956) states that a controller must possess at least as much variety as the system it controls: "only variety can destroy variety." The proposed theory provides a mechanism-level complement to Ashby's law. Ashby answered "how much control is needed"; this theory answers "how control works" — through compression mapping that transfers entropy across dimensions. The entropy leakage concept explains why increasing control in one dimension often fails to improve overall system stability: the entropy does not disappear but migrates to dimensions outside the controller's monitoring scope.

Stafford Beer's Viable System Model (Beer, 1972, 1979) and management cybernetics share the theory's concern with how organizations maintain viability through recursive control structures. The coding evolution framework offers a complementary perspective: while Beer focused on the structural architecture of viable systems, the present theory focuses on the dynamic process by which those architectures evolve.

### 3.3 Ecological Resilience and Panarchy

Holling's adaptive cycle (Holling, 1973) and the panarchy framework (Gunderson & Holling, 2002) describe how social-ecological systems cycle through four phases: exploitation (r), conservation (K), release (Ω), and reorganization (α). The conservation (K) phase corresponds to increasing rigidity in the proposed theory — control accumulates, connections become rigid, and the system becomes vulnerable to shocks that fall outside its narrowed strategy space. The release (Ω) phase corresponds to entropy leakage reaching a critical threshold, triggering a dimension collapse. The reorganization (α) phase corresponds to the formation of new codes.

The key difference is that the proposed theory provides a unified mechanism (compression mapping → entropy leakage) that explains *why* the adaptive cycle occurs, rather than describing *what* occurs. It also extends the domain of analysis beyond ecosystems to include legal systems, programming languages, organizational management, and other code-governed systems.

### 3.4 Institutional Economics and Collective Action

Ostrom's design principles for long-enduring common-pool resource institutions (Ostrom, 1990, 2005) identify structural features — clear boundaries, low-cost conflict resolution, minimal recognition rights, nested governance — that correlate with institutional survival. These principles can be reinterpreted in the proposed framework: clear boundaries define the code's domain; low-cost conflict resolution provides heat dissipation channels; nested governance establishes multi-layer coding architecture. Ostrom's empirical finding that systems satisfying 7-8 principles have >85% long-term survival rates while those satisfying fewer than 3 all collapse (Ostrom, 1990, ch. 3) provides an empirical anchor for the theory's claim that code structure determines system antifragility.

North's institutional change theory (North, 1990) describes how institutions (codes) reduce uncertainty (specific-dimension entropy decrease) while creating new interest conflicts and strategic spaces (entropy leakage to other dimensions). The proposed theory's coding evolution cycle formalizes this dynamic.

### 3.5 Complexity Economics and Agent-Based Modeling

Arthur's complexity economics (Arthur, 2013, 2021) views markets as non-equilibrium, emergence-driven systems where agents continuously adapt their strategies. Beinhocker's (2006) synthesis of complexity science and economics describes economic evolution as a search algorithm operating on a space of "business plans" (codes). The proposed theory aligns with these frameworks but adds a diagnostic dimension: it asks not only "how does emergence happen" but "what kind of emergence is not fragile" — focusing on the dimension distribution of control rather than the fact of emergence itself.

### 3.6 Novel Contributions

While the individual components of the theory have precedents in the traditions above, the following elements represent novel synthesis and extension:

1. **The unified mechanism of control as compression mapping** provides a common language for describing control operations across physical, biological, social, and institutional domains.

2. **The entropy leakage principle** — that total entropy does not decrease, only transfers across dimensions — provides a testable diagnostic for why optimizing one dimension often degrades overall system health.

3. **The three cross-disciplinary fallacy patterns** (coding reversal, dimension compression bias, self-referential closure) identify structural errors that recur across disciplines, offering a meta-level diagnostic that no single-discipline framework captures.

4. **The inversion of "life as entropy resister" to "life as entropy seeker"** provides a new foundation for understanding motivation, innovation, and the dynamics of cultural evolution.

---

## 4. Cross-Disciplinary Analysis: Three Fallacy Patterns

The theory identifies three structural fallacy patterns that recur across eight disciplines. Each pattern stems from the same root cause: the nature of compression mapping as a dimension-specific operation.

### 4.1 Coding Reversal

**Definition:** Each discipline mistakes an operational code for the system's fundamental purpose. The means of measurement becomes the goal of operation.

**Examples across disciplines:**

- **Economics:** The operational code of "individual utility maximization" is mistaken for the purpose of markets, when the purpose is maintaining a transaction system (information exchange) that enables continuous code alignment among participants.
- **Political Science:** The operational code of "one person, one vote" is mistaken for the purpose of democracy, when the purpose is enabling continuous code evolution in the social system.
- **Medicine:** The operational code of "eliminate the pathological target" is mistaken for the purpose of health, when health is a multi-dimensional entropy balance that requires tracking where intervention-induced entropy leaks.
- **Education:** The operational code of "standardized test scores" is mistaken for the purpose of learning, when learning is the formation of an individual's own evolutionary engine.

**Mechanism:** Compression mapping is a reduction operation. When a complex multi-dimensional reality is mapped to a single metric (f: all activities → {one number}), the metric becomes the only dimension that "counts" in the system's decision logic. Over time, the system optimizes for the metric rather than the underlying reality the metric was designed to proxy.

### 4.2 Dimension Compression Bias

**Definition:** Codes inherently favor measurable dimensions. When "only what is measured gets managed" becomes the default operating strategy, immeasurable dimensions — buffers, redundancy, empathy, growth — are systematically ignored.

**Examples across disciplines:**

- **Lean production:** Zero-inventory, just-in-time delivery maximizes efficiency in the measurable dimension of inventory turnover, but eliminates the buffer dimension that absorbs supply-chain shocks. The COVID-19 pandemic revealed the fragility of this optimization.
- **Scientific evaluation:** Impact factors, citation counts, and publication numbers compress all research activity into countable dimensions. Negative results, replication studies, and paradigm-challenging work — essential for science's self-correcting mechanism — are filtered out of the "publishable" category.
- **GDP-centered development:** GDP measures the total value of goods and services but does not measure how many households stand on the "poverty knife-edge" (one emergency away from destitution), the erosion of social trust, or the depletion of natural capital.

**Mechanism:** This is not a failure of individual cognition — it is a structural feature of code-based governance. Codes are, by definition, finite descriptions of control rules. A finite description can only encode a finite number of dimensions. The dimensions that are not encoded do not disappear — they continue to exist and accumulate entropy — but they lose institutional legitimacy because the system has no language to process them.

### 4.3 Self-Referential Closure

**Definition:** All internal critiques within a discipline are resolved within the existing code framework. Economics adds constraints to utility functions; management replaces bad KPIs with better ones; education responds to the shortcomings of standardization with more standards.

**Examples across disciplines:**

- **Economics:** Behavioral economics demonstrates that humans deviate from rational-agent assumptions, but the framework remains "deviation from rationality" rather than questioning whether rationality is the right benchmark. Risk management theory can explain post-hoc why lean production was fragile, but cannot diagnose the fragility before a disaster occurs.
- **Political Science:** Arrow's impossibility theorem proves that no voting system can satisfy all reasonable axioms; public choice theory reveals rent-seeking in voting; deliberative democracy advocates supplementing voting with deliberation. All critiques operate within the assumption that voting is the framework — they describe what is lost, but do not question whether the compression mapping itself is the problem.
- **Management:** Goodhart's Law states that "when a measure becomes a target, it ceases to be a good measure." The management response is to design better KPIs, balanced scorecards, and OKRs — all of which are still codes operating in the measurable-dimension space.

**Mechanism:** A discipline's code framework is also its legitimacy foundation. To question the code is to question the discipline's basis for existence. Internal critiques therefore converge on improving the code rather than replacing it. This is not intellectual dishonesty — it is a structural property of institutionalized codes.

---

## 5. Diagnostic Framework

### 5.1 Three Questions

For any system — a team, a body, a company, a policy — the theory provides a diagnostic protocol of three questions:

1. **Where is control applied?** Identify the compression mappings currently operating in the system. Which dimensions are being compressed?

2. **Which dimensions are approaching their limits?** Entropy never disappears — it transfers. When you compress the attendance dimension (requiring everyone to clock in by 10 AM), where does the displaced entropy flow? Is it leaking into the "spontaneous communication" dimension, the "innovation" dimension, or the "employee well-being" dimension? Assess the remaining heat dissipation capacity of each dimension.

3. **Where is the entropy flowing next?** If a dimension that is already saturated continues to receive entropy, where will it transfer the overflow? Digestive system failure does not cause entropy to explode in place — it transfers to the immune system. Legal department compression does not eliminate compliance risk — it transfers undetected risk to business operations. Tracing entropy flow paths is drawing a collapse roadmap.

### 5.2 PDCA: A Practical Methodology

The Plan-Do-Check-Act (PDCA) cycle, originally developed for total quality management, maps directly onto the theory's operational logic:

- **Plan:** Select a dimension and establish a target state. Ensure the target has sufficient strategy space — do not choose a direction that is already near its rigidity limit.
- **Do:** Apply a compression mapping to converge the affected elements toward the target.
- **Check:** Verify that the compression mapping is effective and that entropy has not leaked into dangerous dimensions. If the compression has introduced new instability (positive Lyapunov exponents), the mapping needs adjustment.
- **Act:** If the compression is successful and stable, solidify it as part of the system's dynamic control rules.

PDCA is a micro-scale implementation of the coding evolution cycle. It enables rapid dimension adjustment without triggering phase transitions — the system evolves through controlled, incremental compression-and-check cycles rather than waiting for environmental selection to force change.

### 5.3 Chinese Medicine as a System-Practice Precedent

Chinese medicine represents a pre-modern system-level diagnostic practice. Without modern analytical instruments, it infers internal entropy distribution from surface signals: tongue coating, pulse characteristics, facial complexion. Acupuncture is not pain relief through chemical intervention — it is a calibrated micro-perturbation on specific meridian dimensions that redirects entropy flow to unblock congested pathways. Herbal medicine adjusts the rhythm of entropy transformation and release, rather than supplementing specific chemical compounds.

The fact that three practitioners may give three different diagnoses for the same patient is not a defect — it is an inherent property of multi-dimensional system intervention. Different diagnoses may be describing different entry points into the same underlying entropy distribution imbalance. The principle of "treating disease before it manifests" (治未病) — detecting entropy circulation deviations through surface signals before symptoms appear — is a direct application of the diagnostic framework to human physiology.

---

## 6. Discussion

### 6.1 What This Theory Provides

The theory does not provide a "correct code" to replace all other codes — that would be self-defeating, as it would itself commit coding reversal. Instead, it provides:

1. **Dimension diagnosis before code operation.** Before any measurement or optimization, ask: What are this system's core survival dimensions? Which are covered by existing codes? Which are neglected? Under what conditions will entropy leakage from neglected dimensions breach critical thresholds?

2. **Codes as evolution objects, not a priori frameworks.** Any discipline's current core codes — utility functions, GDP, blood pressure standards, admission scores — are historical products, not cosmic constants. Codes should iterate with system state changes. In practice, codes acquire institutional inertia because changing them means changing the entire discipline's legitimacy foundation.

3. **Antifragility as a cross-disciplinary meta-standard.** The test of a theory or practice is not what it measures, predicts, or controls — but whether it can maintain core functions under unexpected shocks and obtain structured improvement from those shocks.

### 6.2 Limitations

The theory, in its current form, has several significant limitations:

1. **Qualitative nature.** The framework provides conceptual direction but lacks formalized mathematical definitions, measurement protocols, and quantitative predictions. The claim that "entropy leaks from dimension A to dimension B" currently cannot be operationalized with specific units or thresholds.

2. **No predictive track record.** The theory's diagnostic claims — e.g., that a system with compression mapping applied to its dissipation dimensions will collapse — have not been tested in a prospective, falsifiable study. The case analyses are retrospective.

3. **Scope ambiguity.** The theory claims to cover physics, biology, and social systems under one framework, but the "entropy" in each domain operates at different levels of abstraction. The bridging argument — that the mathematical structure is isomorphic across domains — has not been formally demonstrated.

4. **No empirical calibration.** Unlike Ostrom's design principles (which have been tested against 91+ case studies) or ecological resilience theory (which has identified measurable regime-shift thresholds), the theory has not yet been calibrated against empirical data.

### 6.3 Path to Formalization

The most promising path to formalization is to build on the three empirical anchors identified in the literature:

- **Ecological resilience theory** (Holling, Gunderson) provides the measurable concept of "controlling variables" — the slow variables that determine system behavior. These are the ecological equivalent of the theory's "dimensions." The documented regime shifts in lake eutrophication, coral reef degradation, and rangeland desertification provide measurable thresholds that correspond to the theory's "entropy leakage critical points."

- **Ostrom's design principles** (Ostrom, 1990) provide an operationalized checklist of code structure properties that correlate with institutional survival. These can be reinterpreted as "code antifragility indicators" and tested against the theory's predictions.

- **Innis and McLuhan's media theory** (Innis, 1951; McLuhan, 1964) provides a generative mechanism for why codes become self-locking: the physical structure of the code medium biases what content is easily produced, transmitted, and institutionalized. This explains the mechanism behind the theory's dimension compression bias.

A formalization program could proceed by: (1) defining a multi-dimensional state space for a target system; (2) operationalizing compression mapping as variance reduction in selected dimensions; (3) defining antifragility as the probability of survival under multi-dimensional random shocks; (4) testing the prediction that compression applied to dissipation dimensions reduces antifragility more than equivalent compression applied to control dimensions.

### 6.4 Comparison with Alternative Approaches

The theory's relationship to traditional science is not one of replacement but of complementarity. In domains where control is deep and entropy leakage is minimal — particle physics, orbital mechanics, chemical kinetics — state-derivation methods (predicting outcomes from initial conditions) are highly effective. The theory predicts and explains this: when control is near-complete and leakage is near-zero, risk assessment and state derivation converge to the same answer. In domains where control is shallow and leakage is high — social systems, organizational design, economic policy — state-derivation methods systematically fail because they do not track entropy transfer across unmodeled dimensions. The theory provides a complementary diagnostic tool for these domains.

---

## 7. Conclusion

This paper proposes a unified systems theory built on the single axiom that entropy equals randomness. Control is defined as compression mapping — the operation that transfers entropy across dimensions without reducing total entropy. Antifragility is defined as the system-level balance between rigidity (control intensity) and flexibility (strategy space). Evolution follows a positive-feedback cycle of code formation, code combination, and new code formation.

The theory identifies three cross-disciplinary fallacy patterns — coding reversal, dimension compression bias, and self-referential closure — that recur across economics, natural science, political science, law, medicine, education, artificial intelligence, and management. These patterns are not the result of individual cognitive bias but are structural consequences of code-based governance.

The theory's central practical message is that building healthy systems does not depend on the strength of control — it depends on correctly judging which dimensions need control and which dimensions need to release entropy. The fundamental error behind every system collapse analyzed in this paper is the same: **control was applied to the dimension that should have been releasing entropy, and was withheld from the dimension that should have been controlled.**

The theory is currently qualitative. The next steps toward formalization involve operationalizing the core concepts — compression mapping, entropy leakage, and antifragility — within measurable multi-dimensional state spaces, and testing the theory's predictions against empirical data from ecological, institutional, and organizational systems.

---

## References

1. Ashby, W. R. (1956). *An Introduction to Cybernetics*. Chapman & Hall.
2. Arthur, W. B. (2013). *Complexity Economics: A Different Framework for Economic Thought*. SFI Working Paper.
3. Beer, S. (1972). *Brain of the Firm*. Allen Lane.
4. Beinhocker, E. D. (2006). *The Origin of Wealth*. Harvard Business School Press.
5. Boltzmann, L. (1877). Über die Beziehung zwischen dem zweiten Hauptsatze der mechanischen Wärmetheorie und der Wahrscheinlichkeitsrechnung. *Wiener Berichte*, 76, 373–435.
6. Gunderson, L. H., & Holling, C. S. (Eds.). (2002). *Panarchy: Understanding Transformations in Human and Natural Systems*. Island Press.
7. Holling, C. S. (1973). Resilience and stability of ecological systems. *Annual Review of Ecology and Systematics*, 4, 1–23.
8. Innis, H. A. (1951). *The Bias of Communication*. University of Toronto Press.
9. McLuhan, M. (1964). *Understanding Media: The Extensions of Man*. McGraw-Hill.
10. North, D. C. (1990). *Institutions, Institutional Change and Economic Performance*. Cambridge University Press.
11. Ostrom, E. (1990). *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press.
12. Ostrom, E. (2005). *Understanding Institutional Diversity*. Princeton University Press.
13. Prigogine, I., & Stengers, I. (1984). *Order out of Chaos: Man's New Dialogue with Nature*. Bantam Books.
14. Schrödinger, E. (1944). *What is Life?* Cambridge University Press.
15. Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27, 379–423.
16. Taleb, N. N. (2012). *Antifragile: Things That Gain from Disorder*. Random House.

---

*This white paper is released under CC BY-NC-SA 4.0. First published 2026-05-25. For discussions, please open an issue at the project repository.*
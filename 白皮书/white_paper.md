# Compression, Release, and Evolution: A Unified Systems Theory from Entropy

> **Authors**: [Author Name]
> **Date**: 2026-05-25 (first published) / 2026-06-02 (white paper) / 2026-09-01 (revised)
> **Status**: Concept paper / White paper
> **License**: CC BY-NC-SA 4.0

---

## Abstract

Systems across physics, biology, and society maintain local order by redistributing entropy to other dimensions. We propose a framework anchored in a redefinition of control: not as a target state, but as an ongoing process that transports randomness (entropy) across dimensions via compression mapping (f: X → Y, |Y| < |X|). From this redefinition, entropy becomes the natural descriptive language rather than an external metaphor. Antifragility emerges as an independent property, irreducible to rigidity or flexibility. Coding transforms system evolution into a unified analytical framework, and a causal-hierarchy microfoundation explains why the resulting coding-evolution cycle cannot stop: once codes exist, intervention is entropy decrease, counterfactual combination is entropy increase, and the combinatorial space of codes grows factorially beyond any controller’s reach. The theory identifies three structural fallacies shared across eight disciplines—coding reversal, dimension compression bias, and self-referential closure—and reinterprets the first two as characteristic stallings of the coding-evolution cycle while the third disables the system’s capacity to repair them. A further distinction between material entropy and information entropy locates the limit of incentive-based coordination: dominance rests not on control density but on entropy supply. Applying the framework’s logic to coding evolution itself reveals that the three-beat coding-evolution cycle is the universal paradigm of evolution, a structural consequence of the theory’s own axioms. Formalization and empirical validation remain as next steps.

---

## 1. Introduction

The second law of thermodynamics states that total entropy in an isolated system never decreases. Yet organisms grow, technologies iterate, and civilizations accumulate complexity. This apparent contradiction between the thermodynamic arrow and the arrow of complexification has been a central puzzle since Boltzmann.

Existing resolutions fall into two traditions. Prigogine’s dissipative structures explain how order emerges: in open systems driven far from equilibrium, nonlinear interaction amplifies fluctuations until they lock into a structure that persists only as long as the dissipative flow continues (Nicolis & Prigogine, 1977; Prigogine & Stengers, 1984). Schrödinger’s “negative entropy” explains why an organism must import order from its environment (Schrödinger, 1944). Holling’s adaptive cycle and panarchy framework describes how complex systems cycle through growth, conservation, release, and reorganization (Holling, 1973; Gunderson & Holling, 2002). These traditions capture essential aspects of the puzzle. What they do not supply is a mechanism connecting the thermodynamic roots of order to observable failure modes across disciplines—and, in particular, an account of what happens after a structure has emerged: which of its dimensions are being hollowed out, and whether its own corrective operations can still reach the codes doing the hollowing. This paper takes the emergence of structure as given and analyzes its subsequent survival and evolution; §3.2 states the division of labor with dissipative-structure theory explicitly.

This paper proposes a theory whose core move is a redefinition of control itself. Rather than defining control by its endpoint—a target state reached or a constraint satisfied—we define it as an ongoing process: control is the transportation of randomness across dimensions. The operational mechanism is a compression mapping (f: X → Y, where |Y| < |X|), and the natural language for describing what is transported is entropy, defined axiomatically as randomness. From this process-based definition, we derive antifragility as an independent system property. We argue that coding—the formal expression of control rules—transforms system evolution from domain-specific descriptions into a unified analytical framework. We conclude that evolution is not merely a desirable property of healthy systems; it is the prerequisite for stability itself.

From this mechanism, we develop a diagnostic framework for analyzing system failure. We identify three cross-disciplinary fallacy patterns and trace them across eight disciplines. We propose antifragility—the balance between rigidity (control intensity) and flexibility (strategy space)—as a cross-disciplinary meta-standard for evaluating theories, policies, and institutional designs.

Our approach complements traditional science. Conventional methods ask, “Given initial conditions, what will happen?” (state derivation). Our theory asks, “Given the current distribution of control, which dimensions are being hollowed out by invisible entropy leakage under random shocks?” (risk assessment). The theory finds strongest application in social, organizational, and institutional domains where control is shallow and leakage is high. It aligns with the second law of thermodynamics, draws inspiration from biological evolution and ecological resilience, and aims to derive novel diagnostic predictions for code-governed systems. The derivation across all claimed domains, however, remains a research program rather than an established result. The two paradigms converge where control is deep—particle physics, orbital mechanics—and diverge where it is shallow—social systems, economic policy.

**Roadmap.** Section 2 develops the core theoretical vocabulary: entropy, compression mapping, rigidity, flexibility, and antifragility (§2.1–§2.5); the causal hierarchy that serves as the microfoundation of the coding-evolution cycle (§2.6); the cycle itself and its claim to universality (§2.7); information and empathy as the two-beat dynamics of exchange (§2.8); the control module that routes entropy between subsystems, together with the distinction between material and information entropy and three derived design conditions—redundancy, slack, and fluctuation (§2.9); and meta-coding, the structure that allows a system to revise its own rules (§2.10). Section 3 situates the framework relative to existing theories, including dissipative-structure theory and the causal hierarchy. Section 4 applies the theory diagnostically: three cross-disciplinary fallacy patterns, their correspondence to stallings of the cycle, and the conditions under which a self-referential closure can be opened. Section 5 turns the theory into a diagnostic protocol. Section 6 discusses limitations, a path to formalization, and complementarity with traditional science.

---

## 2. Theoretical Framework

### 2.1 Entropy

A precise description of control requires a language for randomness. We adopt entropy, defined as randomness: the number of distinct states a system can occupy. This is the entropy of dynamical systems theory in its mathematical sense—the size of a possibility space, the growth rate of distinguishable states along a trajectory. Thermodynamic entropy (S = k ln W, where W counts microstates) and information-theoretic entropy (H = -Σ p_i ln p_i) are instances of this same measure in their respective state spaces. The framework takes the shared measure as its base; it is not derived from physical entropy, but treats physical and information entropy as domain instances of the same structure.

A room with books scattered across the floor, glasses on random surfaces, and cables in arbitrary configurations has high entropy. The number of possible arrangements is combinatorially large. After tidying, with every object in a designated position, the room has low entropy in the object-position dimension: only one or a few arrangements correspond to “tidy.”

**Technical and analogical uses of entropy.** This framework uses entropy in two registers. In physical and information-theoretic systems (§3.1), entropy carries its technical definition (consistent with Boltzmann and Shannon) and can be quantified in well-defined state spaces. In social, organizational, and institutional systems, entropy serves as a heuristic concept whose formalization requires first establishing the relevant state-space definition (see §6.3). Both registers share the same conceptual structure—measuring the size of a possibility space—but differ in their degree of operationalization. Throughout this paper, we signal the distinction explicitly when the application domain shifts.

### 2.2 Control as Compression Mapping

**The redefinition of control.** Existing theories define control through its outcome: a system reaches a target state or satisfies a constraint. In this view, control is measured by the state that results. Machines keep temperature within a band; organizations hit quarterly targets; laws maintain social order. Wiener’s cybernetics improved on static definitions by recognizing control as a dynamic process (Wiener, 1948). However, the process it described was the evolution of the controller-how feedback loops adapt over time-not the mechanism of control itself. What computations occur during control? What is being transformed, and into what? In the standard account, control remains a black box labeled “restriction” or “regulation,” described by its endpoint rather than its operation.

We propose a different definition: control is the process of transporting randomness from one dimension to another. It is not the final state of constraint; it is the ongoing act of relocation. The implementing mechanism is a compression mapping:

**f: X → Y, where |Y| < |X|**

A dimension is a coordinate of the system's state space along which states can be distinguished—the analogue of a mechanical degree of freedom. X and Y are sets of distinguishable states along a single such coordinate; compression acts on one coordinate, and the randomness it displaces must reside on the others. Multiple states in the input space X map to the same state in the output space Y. When a team is told to “use Python for the backend,” the programming-language dimension is compressed from dozens of candidates to one. When a recipe specifies “use only three seasonings,” the seasoning dimension is compressed from a large combinatorial space to a small one. The control is not the resulting homogeneity; it is the continuous operation of forcing many possibilities to converge on few.

**Why entropy emerges naturally.** Because control is a process that transports randomness, entropy becomes the natural descriptive language. If control merely produced a final state, entropy would be unnecessary. We could describe control entirely in terms of initial and target states. But once we ask what was done to the randomness during this process, we need to track it. This redefinition does not borrow entropy as an external metaphor; it makes entropy inevitable for describing what control is.

**The critical consequence:** total entropy does not decrease. The randomness removed from the compressed dimension does not vanish. It leaks into dimensions not covered by the mapping. Compressing the seasoning dimension forces more intense innovation in cooking technique, heat control, and ingredient pairing to compensate. Total cooking complexity has not diminished; it has redistributed.

This principle is isomorphic to the second law of thermodynamics: no process reduces total entropy. What appears as entropy reduction in a focal dimension is always accompanied by entropy increase elsewhere. Control is entropy transportation, not entropy elimination.

### 2.3 Rigidity and Flexibility

Compression mapping as the mechanism of control yields two poles on a continuous spectrum of control intensity:

**Rigidity** equals more control. A rigid system applies compression mapping to more dimensions, or applies tighter constraints within a given dimension. The total control quantity is larger, and the remaining strategy space—the set of alternative paths—is narrower. A glass bowl is an extreme case: almost every molecule is locked into a crystal lattice, leaving virtually no strategy space. When dropped, the bowl has exactly one path: fracture along crystal planes.

**Flexibility** equals less control. A flexible system applies fewer compression mappings, or applies looser constraints. The total control quantity is smaller, and the remaining strategy space is wider. A sponge can deform, bounce, and absorb impact because its structure leaves room for molecular rearrangement.

Rigidity and flexibility are neutral descriptive terms. Neither is inherently good or bad. A system is “too rigid” when its strategy space is too narrow to respond to events outside its compressed pathways. A system is “too flexible” when its control is too weak to maintain coherent structure; it ceases to be a system and becomes random drift.

### 2.4 Antifragility

We define antifragility as a qualitative indicator of how much randomness a system can handle in the dimensions it controls. It is not a precise scalar: the randomness-handling capacities of two different dimensions cannot be directly compared. Rather, antifragility provides a direction for reasoning: before any decision, the question is not “Does this make a specific metric more efficient?” but “Does this increase the system’s overall antifragility?” Because the randomness it measures arrives from the environment, antifragility is acquired through interaction rather than produced internally; what a system can design is the size of its exchange surface (§2.9).

**Antifragility is an independent property.** It is not reducible to rigidity, flexibility, or any simple combination of the two. Rigidity describes control intensity; flexibility describes strategy space width; antifragility describes the system's capacity to absorb and metabolize randomness while maintaining core function. These are three distinct axes. The term is borrowed from Taleb (2012), whose usage emphasizes a system’s gain from disorder; the definition here is narrower and structural, specifying the dimension distribution that makes such gain possible. A rigid system may or may not be antifragile depending on how its control is distributed; a flexible system may or may not be antifragile depending on whether its freedom is structured. The practical consequence is that changing rigidity alone-either increasing or decreasing control-cannot guarantee improved antifragility. The diagnostic question is always: which dimensions are being controlled, and which are being starved of entropy-release capacity?

The relationship between antifragility, rigidity, and flexibility is directional rather than definitional:

- **Too rigid**: strategy space is too narrow; the system collapses when a random event falls outside its narrow path. Examples include cancer cells (all control compressed into proliferation, killing the host) and glass bowls (zero strategy space for impact).
- **Too flexible**: control is too weak; the system cannot maintain coherent structure. Example: a team with no task allocation, no quality standards, and no coordination—each member has maximum freedom, but the system as a whole has collapsed.

**Antifragility is defined on the system as a whole, not on individual controls.** Multiple controls can operate simultaneously, but if they counteract each other without forming a coherent force, antifragility does not increase. The art of system design is not maximizing control; it is drawing the correct dimension distribution map: which dimensions need control, and which need room to breathe.

Three common misconceptions:

1. Rigidity is not antifragility. More control narrows strategy space. A stone is extremely rigid but shatters on impact.
2. Flexibility is not antifragility. Removing all control increases freedom but destroys coordination. Antifragility requires both control force and strategy space.
3. Speed and pressure do not equal optimality. Acceleration increases entropy production; simultaneous control increase narrows the dissipation channels. The result is internal entropy accumulation and eventual burnout, analogous to placing an air conditioner’s outdoor unit inside the room.

**Operational form.** Within this framework, an antifragility assessment takes the comparative form: under shock X, does the system's core function survive, degrade, or improve? The answer is directional (“more antifragile than” rather than “antifragility score of N”) and specific to the dimensions being shocked. An antifragility claim is disconfirmed if a system exposed to a specified class of random shocks in a specified dimension exhibits degradation of core function rather than maintenance or improvement. The comparative form is the definitional one; a scalar summary—for instance, the probability of maintaining core function under a specified shock distribution—is a possible formalization (§6.3) rather than an equivalent definition. Where a scalar is used below, it is shorthand for the comparative claim.

### 2.5 System, Subsystem, and Heat Dissipation

A system is a set of elements operating under shared control, forming a coherent whole. It is not a static object but a continuous process of control maintenance. A band is not “four people with instruments”; it is those four people continuously playing according to a shared score. When the playing stops, the system ceases to exist.

Every system must release entropy to its environment. Maintaining low entropy in certain dimensions—order—necessarily produces high entropy in others. If the entropy-production rate exceeds the heat dissipation bandwidth—the capacity of available dimensions to absorb and release entropy—the system accumulates entropy internally until it collapses. A system that runs faster produces more entropy and requires more dissipation bandwidth. Speed without bandwidth expansion makes a system more fragile, not stronger.

Dissipation bandwidth is bounded in two distinct senses. First, not every dimension can serve as an outlet: a building's waste heat can be discharged into the air, but the communication friction accumulated between teams has no external port, and must be discharged internally, onto dimensions such as turnover, schedule slippage, and morale that can absorb more before they fail. Second, those dimensions that can serve as outlets have finite capacity. A river carries ordinary rainfall; it does not carry a flood. Collapse occurs when the rate of entropy production exceeds the rate at which available dimensions can release it—which is why adding control without widening dissipation is a net loss.

A subsystem exists within a parent system. In some dimensions, the subsystem maintains low entropy not through its own control but because the parent system provides it. A cell does not regulate its own temperature; the organism does. This arrangement is also the subsystem’s vulnerability: if the parent system fails, the subsystem collapses in those dimensions. The routing of entropy between subsystems, and the conditions under which that routing can keep changing, are treated in §2.9.

### 2.6 The Causal Hierarchy as Microfoundation

Section 2.7 will claim that the coding-evolution cycle—new codes, new combinations, newer codes—is the universal paradigm of evolution. That claim requires a microfoundation: an account of why the cycle necessarily turns, rather than being an empirical generalization that happens to hold in the cases examined. The microfoundation comes from the causal hierarchy, translated into the language of control.

Pearl distinguishes three levels of causal capacity (Pearl, 2009; Pearl & Mackenzie, 2018). The first is association: observing that variables co-vary, P(Y | X). The second is intervention: actively changing a variable, P(Y | do(X)). The third is counterfactual: reasoning about what would have happened under conditions that were never observed, P(Y_X | X', Y').

Translated into the present framework, the three levels are three stages of control:

- **Level 1 (association)** is observation without codes. The system registers signals but imposes no constraint on any dimension. There is no control and therefore no entropy transport.
- **Level 2 (intervention)** is compression mapping. To intervene is to constrain a dimension—to reduce the randomness in that dimension and displace it elsewhere. This is entropy decrease in the targeted dimension, and it is where control begins.
- **Level 3 (counterfactual)** is entropy increase in code space. A counterfactual requires assembling a combination of codes that has never been experienced: a system that has only known “the X I did produced the Y I saw” cannot represent “the X I never did, together with the Y I never saw.” That representation demands that X and Y be codes rather than sensory traces, and it demands that they be recombined in a configuration with no experiential precedent. Counterfactual reasoning is combinatorial entropy increase over codes.

This mapping carries three consequences.

First, **intervention and counterfactual are not two faculties but two halves of one cycle.** Level 2 is the first beat of the coding-evolution cycle: a new constraint forms. Level 3 is the second beat: the combinatorial space opens. The cycle of §2.7 is the causal hierarchy seen in motion.

Second, **the second beat is not optional.** Once codes exist, the space of their combinations is factorial in the number of codes, and no controller can cover a space of that size with constraints. Counterfactual combination is therefore not an accidental by-product of intelligence; it is what happens whenever codes exist and are operated on. Section 2.7 uses this fact to replace the weaker argument that the cycle is universal because “the code-space contains only codes.”

Third, **the definition of life is consistent across both frameworks.** This theory defines life by entropy-seeking and evolution (§2.7), where entropy-seeking is the form that the maintenance condition takes once selection is possible. The causal hierarchy defines life by the capacity to intervene: a stone weathering into sand is not a do(X) operation, and only a system that alters its environment in response to feedback possesses the rudiments of causal perception. The two definitions are not rivals. Intervention is the precondition for sustained entropy intake: a system must act on its environment to keep acquiring the novelty it metabolizes. Conversely, a system with intervention capacity but no entropy-intake loop would exhaust its own operating margin and vanish on a timescale too short to observe. The two definitions therefore pick out the same set of persistent systems.

Two boundaries are worth marking. First, as it appears in natural evolution the hierarchy is ordered bottom-up: intervention precedes language, and language—a code-generation system—compresses counterfactual reasoning from the timescale of genetic generations to the timescale of a single brain. Each new code creates a new dimension in which counterfactuals can be assembled, which is why the accumulation of codes accelerates the cycle. Second, the hierarchy is not a ceiling on control. Algorithmic reasoning—the Turing machine, and formal systems generally—sits above Level 3, since it computes without needing to have observed or imagined the case at hand. In natural evolution the order is bottom-up; in the development of human tools it has run top-down, from formal logic back to systematic verification. Both orders converge on the same point, where formal derivation proposes hypotheses, counterfactual reasoning constructs scenarios, and intervention verifies results.

### 2.7 Coding and the Universal Paradigm of Evolution

Sections 2.1–2.5 established what control is and how systems maintain it. They showed that control operates through compression mapping, the balance of rigidity and flexibility, and the management of heat dissipation. But systems do not merely maintain control; they also change. The question driving the remainder of the framework is: how do systems evolve, and is there a universal language for describing that evolution?

**Why coding.** To study how systems evolve, we need a common language for describing what evolves. A system’s control rules—its regulations, syntax, genetic code—constitute its coding: the formal expression of control. An organization’s regulations, a programming language’s syntax, a species’ genome: these are all codes. The philosophical idea that a formal symbolic system can capture the structure of a domain has a recognized precedent in Wittgenstein’s picture theory of language (Wittgenstein, 1922), which argued that propositions picture facts through shared logical form. In the present framework, however, codes are not mere representations; they are the operational rules that actively govern a system’s entropy distribution.

The move from studying individual system evolutions to studying code evolutions is the theory’s key methodological contribution. Without coding, each system type requires its own evolutionary language. Biological evolution proceeds through mutation and selection, legal evolution through precedent and legislation, technological evolution through design and iteration. These operate with separate vocabularies, separate communities, and separate methods. Coding collapses this diversity into a single analytical framework: a genome mutation, a contract clause, and a software patch are all the same operation—a code modification that alters entropy distribution—and each can be analyzed with the same tools. This unification enables the cross-disciplinary analysis in Section 4 and makes the theory a usable diagnostic instrument rather than merely a philosophy of systems.

**The coding-evolution cycle.** Once systems are described through codes, their evolution follows a single positive-feedback dynamic:

> **Entropy decrease (new codes) → Entropy increase (new-old combinations) → New entropy decrease → ...**

The first half-beat is entropy decrease. A new code forms: a constraint that reduces randomness in a specific dimension of expression. Poetic form is itself a code—it governs which combinations of syllables, tones, and imagery are permissible—and the history of poetry is a history of codes evolving. The Tang Dynasty’s regulated verse (*jueju*) imposed strict syllabic and tonal constraints on poetry—a compression mapping on linguistic expression.

The second half-beat is entropy increase. The new code combines with existing codes, generating an explosion of combinatorial possibilities. The constraints of regulated verse, far from killing poetry, forced poets to explore imagery, inversion, and wordcraft in dimensions everyday language never needed. The information density of regulated verse far exceeds that of ordinary speech.

The cycle then repeats: new combinatorial richness exposes new dimensions that need control, prompting the formation of yet newer codes. Song Dynasty *ci* poetry loosened some constraints; modern free verse loosened others. Each relaxation triggers a new round of entropy increase on the combinatorial dimension, followed by new constraints.

This cycle operates without a conscious “coder.” Galactic disks are a telling instance: gravitation compresses matter along the rotation-axis dimension—a compression mapping without a designer—and the displaced randomness regenerates in the plane-of-disk and momentum dimensions. The disk as a whole is a maximum-entropy state of the gravitational system; overall entropy increase does not preclude local entropy decrease in a sub-dimension, and the two are the same process at different granularities. Human-designed codes (laws, programming languages) and spontaneously emerged codes (physical laws, market conventions) both instantiate the same mechanism.

Why does this cycle never stop? Every round of entropy decrease—gaining control—necessarily produces more entropy in the code-usage dimension. More entropy means more randomness, which creates new control demands—a positive feedback loop. In plain terms: every new rule creates situations the old rules did not cover, which forces the creation of yet more rules. There is no terminal state of “perfect control”: the combinatorial space of code interactions grows factorially with the number of codes, far exceeding any control system’s capacity to cover.

**Why the cycle is universal.** The three-beat form of the coding-evolution cycle is not merely an empirical observation; it is a structural consequence of the theory’s own logic, and §2.6 supplies the mechanism. When coding evolution is itself analyzed as a system, the “dimension” being operated on is the code-space itself—the set of all possible control rules. A compression mapping on this space takes the form of a new code: a constraint that reduces the entropy of expression in some sub-dimension. Forming new codes is not merely one way to control the code-space; it is the only viable one, because the code-space contains only codes and their interactions. Any control operation on this space—including a meta-level constraint on which codes are permitted—is itself describable as a code and therefore constitutes another compression mapping on the code-space. There is no operation available at this level that is not a code.

That establishes why the first beat must take the form of a new code. The second beat follows from the same structural fact by way of the causal hierarchy: the entropy displaced by this compression is released into the code-combination dimension, and once a combination dimension exists, counterfactual assembly over it is unavoidable (§2.6). The three-beat cycle is therefore the universal paradigm of evolution, a structural consequence of the theory’s own axioms rather than an inductive generalization. If the paradigm is universal, any complex adaptive system—including life—should be analyzable as an instance of it.

**Evolution as a system.** The process of evolution can itself be analyzed through the theory’s lens, with its own control mechanisms, strategy space, and antifragility. Natural selection is the rigid face: a compression mapping that eliminates unfit individuals, converging the population toward adaptive states. Genetic drift (random variation) is the flexible face: small-scale random perturbations that explore adjacent possibilities. Recombination operates at the code level, splicing code fragments to produce new combinations, which selection then filters. A healthy evolutionary system requires balance: excessive drift makes convergence too slow (too flexible); excessive selection pressure flattens diversity (too rigid); rich recombination with moderate selection yields both strategy space and filtering efficiency.

Evolution also evolves its own mechanisms. The transitions from asexual to sexual reproduction, from purely genetic transmission to cultural transmission (language), and from waiting for real mutations to counterfactual reasoning each represent a meta-level compression mapping on the “means of evolution” dimension. These create new layers of control that dramatically accelerate the evolutionary cycle.

If the coding-evolution paradigm is universal, then any complex adaptive system—including life itself—should be analyzable as an instance of it.

**Life as an instance of the paradigm: entropy-seeking as a phenomenon.** Schrödinger described life as feeding on “negative entropy,” absorbing order from the environment to maintain internal order (Schrödinger, 1944). The present framework does not invert this; it specifies what the flow becomes at a higher level. Because a structure persists only while the dissipative flow continues (§3.2), any system still maintaining itself must simultaneously take in from its environment and discharge to it. At the lowest level that intake is uniform and passive: a convecting fluid, a forming cloud. Nothing is “looking.” At the level of an organism the intake is no longer uniform—not any substance, not any stimulus will do—and selection requires a mechanism of direction. From the outside, this appears as actively going to look for something, which is what “entropy-seeking” names. It is therefore not an additional postulate but the form the maintenance condition necessarily takes once a system is capable of selection; it looks like a purpose because selection needs a direction, and a direction seen from outside is an orientation. Dopamine is the navigational mechanism that this level requires (Schultz, 1998), signalling not a reward already delivered but a direction in which something new may lie. In the same division, “negative entropy” names the discharge end of the flow and “feeding on entropy” the intake end: what enters is not order but randomness that the system has not yet metabolized. This remains a hypothesis open to empirical test in its mechanism, but its structure follows from the framework rather than being borrowed. From the theory’s perspective, life is not a special case; it is one instance of a universal coding-evolution cycle operating on a particular substrate, observed at the level where selection appears.

**Nested levels of evolution.** Because evolution is itself a system, its mechanisms can themselves evolve. Each transition in the table below adds a layer of control over the previous layer's means of evolution, and each layer buys antifragility at the cost of a new vulnerability.

| Level | Evolutionary system | Control mechanism (compression mapping) | Strategy space (source of variety) |
|---|---|---|---|
| L1 | Individual adaptation | Gene-expression regulation | Phenotypic plasticity |
| L2 | Population evolution | Natural selection (drift, recombination, selection) | Genetic diversity |
| L3 | Evolution of evolutionary means | Asexual to sexual reproduction; genetic to cultural transmission | Diversity of evolutionary mechanisms |
| L4 | Cognitive acceleration | Language coding, counterfactual reasoning, design-based evolution | Space of conceivable possibilities |

The transitions are not designed; they are what survives. Each one also creates a new class of fragility: language coding can be distorted, cultural coding can petrify, counterfactual reasoning can detach from its referent. The next layer of evolution typically arises to handle the vulnerability introduced by the previous one, which is why the nested cycle has no terminus.

**A note on the term “entropy.”** Throughout this paper, entropy denotes the size of a possibility space, in the sense shared by Boltzmann's S = k ln W and Shannon's H = -Σ p_i ln p_i. In physical and information-theoretic contexts the quantity is well defined and measurable; in social and organizational contexts it functions as a heuristic whose formalization requires first specifying the state space (§6.3). The two registers share the same structure—both measure the size of a possibility space—but not the same degree of operationalization. A reader who imports the thermodynamic reading wholesale will misjudge the framework's social claims in both directions: treating heuristic statements as if they carried units, or dismissing structural claims for want of them.

---

### 2.8 Information and Empathy

Control moves entropy across dimensions; information is what travels when two systems exchange it. This section defines information and derives the two-beat structure of empathy from the framework's own vocabulary.

**Information as constrained combination.** Information is not signal volume. A signal becomes informative only within a code: a set of constraints determining what may count as a signal, what it may combine with, and what it means. A fluctuation with no code to receive it is noise. Codes therefore do double duty in exchange: they make information possible by restricting the space of admissible signals, and they bound the meaning of any given signal to what the code can represent.

**Empathy as two beats.** Empathy—understood here as the measured efficiency of exchange between two systems rather than as a moral attitude—decomposes into exactly the two beats of §2.7.

- **Code alignment (entropy decrease).** Two systems share a code: a language, a vocabulary, a set of mutual expectations, a common aesthetic. Alignment is a compression mapping, since shared code allows the sender to omit what the receiver can reconstruct. The higher the density of shared code, the lower the energy cost per unit of exchange. This is why meeting a compatriot abroad, or catching a joke inside a profession, registers as rewarding before any content has been exchanged: what is registered is the collapse of exchange cost, not the content.
- **Novel combination (entropy increase).** Alignment builds the channel; it does not fill it. Exchange must then carry combinations that have not previously been ingested. A channel that transmits only repetitions produces no entropy intake. This is the systemic reason the tenth telling of the same anecdote ceases to please: an aligned code plus an already-ingested combination yields zero new randomness, and the exchange registers as pure cost.

Either half alone is insufficient. Without alignment the channel cannot open. With alignment but without novel combinations, the channel idles and the relationship decays. Empathy is sustained only when both beats alternate.

**Persona as compression mapping.** Because the value of a single message cannot be assessed before it is received, systems select sources rather than messages. A source is predictable to the extent that its outputs are constrained: a public figure has a stable content boundary, a friend a stable framework of judgment, a publication a stable spectrum of topics. This stable constraint is what we call a persona, and in the framework's terms it is a compression mapping from all producible information to that which conforms to the persona: f(all producible output) → {persona-conforming output}. Two effects follow in opposite directions. A narrow persona has a lower probability of matching any given receiver but a deeper alignment when it does. A persona is therefore a control decision trading coverage for depth.

A further cost runs in the same direction: the tighter the persona, the larger the accumulated tension at the boundary of the constraint, and the more consequential a rupture. When intake exceeds what the framework can metabolize, entropy does not exit through the normal channel; it strikes the boundary itself. The result is not merely a negative event but a loss of trust in the stability of the source's code—and where the rupture falls on a morally load-bearing dimension, it can dissolve the framework wholesale. The tightest constraint is the most fragile node.

**Productivity of entropy.** Alignment is a one-time construction cost; sustained intake depends on how much genuinely new combination the channel carries per unit time. Volume is not entropy: a source publishing ten items a day that recombine the same code in the same way delivers zero. Emission frequency and novelty share a single axis, whose product is the intake rate.

**Directionality: entropy increase can accommodate entropy decrease, not the reverse.** Empathy operates on entropy increase; instrumental exchange operates on entropy decrease. Control does not produce entropy decrease in a targeted dimension out of nothing; it displaces entropy onto other dimensions. This asymmetry fixes the direction of the relationship. A receiver whose drive is entropy increase in the empathic dimension can accept control on other dimensions, because the displaced entropy flows toward the dimension it wants fed: constraint becomes a tool of intake. The reverse does not hold. If the receiver's objective is entropy decrease in a specific dimension—a definite output, a fixed deliverable—then entropy increase elsewhere in the system does nothing for that objective, because entropy does not flow backward to compress the targeted dimension. The commonly observed asymmetry that empathy can motivate instrumental cooperation while instrumental framing cannot manufacture empathy is thus a structural consequence rather than a cultural norm.

**Why the empathic code must keep evolving.** Alignment is bounded in time for the same reason any code is: the combination space of a fixed code is finite, and repeated intake drives its marginal entropy toward zero. Sustained empathy requires the code itself to expand. The loop repeats the three-beat form: new codes sediment (shared experiences), existing codes recombine (new topics, new understandings), and successful combinations settle back into the code (in-jokes, agreed premises). In most existing systems the two operations run sequentially—sediment, then combine. The cycle runs faster where they interleave, so that new codes meet old codes during combination rather than after it. Frequency and cross-penetration, not the mere existence of a loop, determine how fast it turns.

---

### 2.9 Subsystems, the Control Module, and Two Entropy Channels

Sections 2.1–2.5 treated control within a single system. Real systems are composed of subsystems, and composition introduces a routing problem. This section derives the control module, the two channels by which a parent system directs its subsystems, and three design conditions that follow from the coding-evolution cycle.

**Routing requires a shared diagram.** A code is the recorded form of control: it specifies which dimension is compressed and to what degree. Each subsystem therefore has its own control code. When subsystems form a parent system, entropy handled by one subsystem must flow to another, and that flow requires a code specifying what moves, from whom, and to whom. This cross-subsystem routing code is the control module—effectively a diagram of the parent system's internal entropy flows.

If every subsystem followed only its own code, two codes could claim the same input dimension: code A routes entropy X from itself to Y, while code B routes the same X to Z. Both compression mappings would then execute on the same dimension and interfere, each spending control capacity neutralizing the other's action rather than processing entropy. This is control coupling: control force consumed by internal friction, subtracted from the capacity available to handle environmental entropy.

Multiple independent diagrams therefore produce overlap, and overlap produces friction. Since independent diagrams are the initial condition rather than a choice, selection does the work: under periodic environmental shocks, systems with heavy overlap have less capacity available for environmental entropy, hence lower antifragility, and perish sooner. Surviving systems converge on non-overlapping control domains. That convergence is the unified diagram, and the function that maintains it is the control module. Any system that persists long enough to be observed therefore runs a single diagram; multiple diagrams describe a non-equilibrium state that selection removes.

This derivation also constrains the origin of leadership. Among subsystems of comparable control capacity—animal groups, human organizations, states—a unified diagram does not appear spontaneously. Some subsystem must take on the work of composing and maintaining it. That subsystem is the leader, and it can perform the work only if the diagram has sufficient authority over the others: with sufficient authority the diagram is a plan, and with insufficient authority it degrades into a suggestion, which in operational effect means multiple diagrams. Long-lived systems therefore contain a subsystem with sufficient authority and a structure that sustains it; systems without it were eliminated by friction. Where two subsystems accumulate comparable authority, the outcome depends on whether the gap in authority can widen before friction consumes the system. If it widens, one prevails; if it does not, the system either collapses or splits into two systems, each carrying its own diagram. That long-lived systems evolve fixed mechanisms for leadership succession—duels among animals, abdication, election, inheritance law—follows from the same logic: these mechanisms compress a competition for authority into a bounded window instead of leaving the system in prolonged internal friction. They are selection products, not ornaments of civilization.

**Two channels of compliance.** A diagram specifies how entropy should be routed; whether subsystems comply is a separate question. Compliance rests on two mechanisms. The first is entropy supply: a subsystem that processes entropy along the specified route receives entropy, and one that does not, does not. Entropy allocation is itself the incentive to follow the diagram. The second is information coding: when the diagram changes, the parent system must signal the change, and the subsystem must receive and act on it. The two channels coincide in simple systems with weak subsystem control capacity—energy in, machine runs, and the energy flow is the whole instruction. In complex systems they separate: subsystems interpret, ignore, or misread signals, and entropy supply may be mediated by a general equivalent—money—that converts heterogeneous kinds of entropy into a single measurable signal. The effectiveness of a diagram depends on whether both channels remain open.

**Material entropy and information entropy.** The separation of the channels is only the first consequence of complexity. The two kinds of entropy have different ceilings.

| | Material entropy | Information entropy |
|---|---|---|
| Ceiling | Bounded (physical constraints) | Unbounded (codes recombine freely) |
| Mechanism inside the organization | Control, typically via a general equivalent | Direct exchange |
| Binding constraint | Real-world productive capacity | Richness and cross-penetration of the code framework |

A general equivalent compresses the allocation problem—f(all types of material entropy) → {monetary units}—and thereby reduces the parent system's coordination cost dramatically. It also splits entropy-seeking in two. Without a general equivalent, acquiring material entropy and participating in coordination are one act: the hunt is shared and the catch divided on the spot. With one, acquisition splits into an internal segment, in which executing along the diagram yields currency, and an external segment, in which currency is exchanged for goods. The internal segment operates on control logic; the external segment operates on entropy increase. Only the second is intake.

The consequence is a statement about authority that does not follow from control density: **dominance rests not on how tightly a system controls, but on how well it supplies entropy.** A system whose only channel is a general equivalent has compliance that fluctuates with material entropy: in abundance the round closes, and in contraction it breaks, at which point subsystems downgrade their participation or leave. A system that can also generate information entropy through shared codes has a second channel that keeps the diagram operative while material entropy is depressed, because the ceiling on that channel is the richness of the code framework rather than productive capacity. Long-term viability, in this framework, means that information-entropy supply covers the troughs of material-entropy fluctuation.

**Three design conditions.** Because the target is not a well-routed diagram but a diagram that can keep evolving, the coding-evolution cycle supplies criteria for any proposed change. Three conditions follow, each tied to a different beat.

- **Redundancy.** A change that depends on a single route—all entropy passing through one subsystem—fails entirely when that subsystem fails, and the cycle stops with it. Comparable transfers must retain multiple competing routes rather than being consolidated into one. Redundancy protects the second beat: without an alternative route, the combination space has nowhere to open.
- **Slack.** Two directions. First, a change whose magnitude exceeds what subsystems can absorb without expending substantial entropy on self-adjustment will consume capacity that could have gone to the parent system's other dimensions; the parent must supply that entropy, and the cost rises with the size of the conflict. Second, exploration requires surplus: if entropy supply is tuned to each subsystem's exact current need, the margin available for probing uncertain paths disappears. Slack is therefore both a bound on the size of a step and an obligation to supply more than the current requirement.
- **Fluctuation.** If entropy is supplied at constant intensity with constant precision, no subsystem can demonstrate that it is more efficient than another, and selection pressure vanishes. Periodic variation restores it: abundance permits experimentation, scarcity eliminates the inefficient. Uniform supply is equivalent to no selection, and the third beat is suppressed.

**Antifragility is acquired through exchange, not designed.** Antifragility was defined in §2.4 as how much randomness a system can handle in the dimensions it controls. Randomness arrives from the environment, which means antifragility cannot be manufactured internally: a system with no exchange surface receives no randomness to handle, so its capacity is neither tested nor increased. What can be designed is the size of the exchange surface, and that is what the three conditions above describe. Redundancy preserves multiple routes through which exchange can occur. Slack preserves the margin that exploration consumes, and exploration is exchange. Fluctuation lets environmental signals actually participate in selection rather than serving as decoration. A system that shrinks its exchange surface—fewer channels, no margin, supply held constant—is not becoming more efficient. It is lowering the ceiling on the antifragility it can ever possess, and it will discover the new ceiling only when a shock exceeds it.

The three conditions map onto the beats with some precision: redundancy governs whether the second beat can proceed at all, slack governs how much capacity remains to conduct it, and fluctuation supplies the third beat. As any of them degrades, the probability that the cycle survives declines—not because control is too weak, but because control has consumed the space in which the cycle operates.

---

### 2.10 Meta-Coding and System Identity

Two questions remain from the framework's definition of a system. If a system is a set of elements under shared control, what holds its identity across time? And what structural feature allows a system to revise the codes that define it—the operation §4.5 identifies as the exit from self-referential closure?

**Identity resides in control, not substrate.** Because a system is defined as elements under shared control, its identity is carried by the control code rather than by the elements it happens to organize. The atoms composing a human body are largely replaced over a decade, yet the person persists. The ship of Theseus is not a paradox under this definition: identity resides in the building and maintenance codes, so a hull replaced according to the same specification is the same ship. Material substrate is a replaceable carrier; the code is the identity.

**Continuity is evolutionary, not static.** The code that carries identity is not fixed. Every new understanding, every persuasive conversation, rewrites it. What sustains identity across time is that the control code remains continuously revisable—that the process of revision is not interrupted. Continuity is a property of the trajectory rather than of a snapshot; memory records the trajectory but is not its substrate.

**Meta-coding.** A control code describes how a system operates. When a system also holds a code describing its own control code and is authorized to modify it, the system possesses meta-coding. The clearest example is a program that reads and rewrites itself: its behavior is no longer derivable from the logic that was written for it, and unless the self-modification settles into a regular pattern, its next step cannot be predicted from outside. Meta-coding is the structural precondition for §4.5: a system can escape a self-referential closure only if some part of it is authorized to modify the code generating the closure. It is also the formal counterpart of the leader in §2.9—the subsystem authorized to revise the diagram—and the reason the “modifiable diagram” there is a structural type rather than an option.

**Death as a phase transition.** If identity resides in control, then the termination of control is a phase transition from system to non-system. At that point, low entropy in the critical dimensions is no longer actively maintained, the control framework dissolves, and what remains is a collection of matter with physical probabilities but no control bias. Entropy continues to increase; what has ceased is the operation that was transporting it.

---

## 3. Relation to Existing Theories

The proposed framework integrates and extends several established intellectual traditions. It does not seek to replace them; it provides a common language for identifying what they share.

### 3.1 Thermodynamics and Information Theory

The theory's definition of entropy follows the dynamical-systems measure of possibility-space size (§2.1); thermodynamic entropy (Boltzmann, 1877; Gibbs, 1878) and information-theoretic entropy (Shannon, 1948) are instances of it in their respective state spaces. The shared structure—a functional that is additive, convex, and positive-definite, measuring the size of a possibility space—supports the extension to social, organizational, and institutional systems. In these contexts, the "possibility space" refers to the set of behaviors, strategies, or states available to agents. The extension is not a category error: category errors concern quantities carrying different dimensions, and physics itself groups quantities with different units under one concept when the structure is shared, as critical temperature and Curie temperature describe the same class of transition. What the extension does require is that each domain specify its state space before quantitative claims are made (§6.3).

### 3.2 Dissipative Structures: Base Completion and Difference in Subject

Prigogine's theory of dissipative structures answers a question this framework takes as given: how does order arise? In an open system driven far from equilibrium, nonlinear interaction amplifies fluctuations, and above a threshold a fluctuation becomes locked into a macroscopic structure—Bénard convection cells, a laser mode, a chemical oscillation—that persists only as long as the dissipative flow continues (Nicolis & Prigogine, 1977; Prigogine & Stengers, 1984). Order is not imposed from outside; it self-organizes out of randomness.

The relationship between the two frameworks is complementarity along a time axis, and it runs in two directions.

**What dissipative-structure theory completes.** The present framework starts from nonlinearity and derives that randomness is unavoidable: under nonlinear interaction, deterministic systems exhibit sensitive dependence on initial conditions. Chaos is not randomness itself—trajectories remain deterministic and retain structure on short horizons—but chaotic dynamics typically generate effective randomness in practice, since long-run behavior becomes unpredictable. The step from “randomness is unavoidable” to “structure exists” was, in earlier formulations of this framework, asserted rather than derived. Dissipative-structure theory supplies the missing mechanism: driven far from equilibrium, fluctuations are amplified and then locked in, so that randomness is not merely the residue that survives control but the raw material from which structure forms. The framework's later stages also inherit the thermodynamic language—order is local, total entropy still increases, structure requires continuous throughput—which states the same thing as “control transports entropy” and “dissipation bandwidth is finite,” expressed in the vocabulary of physics.

**Where the two frameworks differ.** The difference is the subject of study.

| | Dissipative-structure theory | This framework |
|---|---|---|
| Subject | Birth of structure | Survival and evolution of structure |
| Starting point | No structure yet; how does randomness organize? | Structure already exists; how is it maintained and changed? |
| Controller | None; physical self-organization without a designer | Present; some party applies control |
| Position in time | Before emergence | After emergence |
| Language | Physical and dynamical, with equations and thresholds | Cross-domain abstraction, descriptive |

Dissipative-structure theory answers how order emerges from disorder. This framework asks how an emerged structure survives, avoids collapse, and keeps evolving.

**The step this framework adds.** Dissipative-structure theory establishes that the flow must exist. This framework asks whether the flow can persist, which resolves into two operations. The first is finding an outlet: every system that maintains order continuously produces entropy, and the question is whether there is somewhere for it to go—what dissipative-structure theory calls an entropy flux and this framework calls dissipation bandwidth. The second is keeping the outlet renewable: outlets are not permanent. Environments change, and today's exit may fail tomorrow. Ensuring that entropy always has somewhere to go, and that the system keeps acquiring new paths, is the work of the evolution mechanism—the cycle of new constraints, new combinations, and newer constraints. Finding an outlet is passive drainage; keeping outlets renewable is active regeneration. The second operation is what this framework adds.

### 3.3 The Causal Hierarchy

Pearl's hierarchy of causal capacity (Pearl, 2009; Pearl & Mackenzie, 2018) is the framework's closest neighbor in the philosophy of causation, and §2.6 uses it as the microfoundation of the coding-evolution cycle. The relationship is worth stating in its own right, because the two hierarchies are often read as competitors.

| Level | Causal capacity | Operation | Translation here |
|---|---|---|---|
| L1 | Association | P(Y \| X) | Observation without codes; no control |
| L2 | Intervention | P(Y \| do(X)) | Compression mapping: entropy decrease in a dimension |
| L3 | Counterfactual | P(Y_X \| X', Y') | Combinatorial entropy increase over codes |

The translation is not a relabeling. It identifies L2 with the first beat of the coding-evolution cycle and L3 with the second, which makes the cycle a description of the causal hierarchy in motion rather than a separate construct. It also explains why L3 rates as a paradigm shift rather than an increment: counterfactual capacity allows a system to posit hidden variables—mediators never observed—and then intervene on them, converting direct control into indirect control. Agriculture, animal husbandry, and water engineering all depend on controlling variables that were inferred rather than seen.

Two clarifications. First, the framework does not require that L3 be grounded in probability calculus. Most everyday counterfactual reasoning is Boolean and categorical—“had I not left the house, I would not have met him”—and the logical connectives carried by language are sufficient. This is why counterfactual capacity does not require the numerical machinery that probabilistic counterfactuals demand. Second, formal and algorithmic reasoning sits above L3, since a Turing machine can compute cases it has neither observed nor imagined. The hierarchy is therefore not a ceiling. Natural evolution traverses it bottom-up, from intervention to language to formal inference; the development of human tools has run top-down, from mathematics back to systematic verification. The two directions converge, and the convergence point—derivation proposes, counterfactual constructs, intervention verifies—is where modern science operates.

This section also marks the framework's boundary with mechanistic causal inference. Pearl's apparatus answers what can be identified from data under a given graph. This framework asks which dimensions a system's control is hollowing out, and whether the system can still modify the codes doing the hollowing. The two are complementary: identification concerns what a given structure implies, and the present framework concerns whether that structure can persist.

### 3.4 Cybernetics and Control Theory

Ashby’s Law of Requisite Variety (Ashby, 1956) states that a controller must possess at least as much variety as the system it controls: “only variety can destroy variety.” The proposed theory provides a mechanism-level complement to this principle. Ashby answered how much control is needed; this theory answers how control works, through compression mapping that transfers entropy across dimensions. The entropy-leakage concept explains why increasing control in one dimension often fails to improve overall system stability: entropy does not disappear; it migrates to dimensions outside the controller’s monitoring scope.

Stafford Beer’s Viable System Model (Beer, 1972, 1979) and management cybernetics share the theory’s concern with how organizations maintain viability through recursive control structures. The coding-evolution framework offers a complementary perspective: Beer focused on the structural architecture of viable systems; the present theory focuses on the dynamic process by which those architectures evolve.

### 3.5 Ecological Resilience and Panarchy

Holling’s adaptive cycle (Holling, 1973) and the panarchy framework (Gunderson & Holling, 2002) describe how social-ecological systems cycle through four phases: exploitation (r), conservation (K), release (Ω), and reorganization (α). The conservation (K) phase corresponds to increasing rigidity: control accumulates, connections become rigid, and the system becomes vulnerable to shocks outside its narrowed strategy space. The release (Ω) phase corresponds to entropy leakage reaching a critical threshold, triggering dimension collapse. The reorganization (α) phase corresponds to the formation of new codes.

The key difference is explanatory ambition: the proposed theory provides a candidate mechanism—compression mapping followed by entropy leakage—that may explain why the adaptive cycle takes the form it does, rather than merely describing what occurs. This hypothesis requires formal demonstration. The theory also extends the domain beyond ecosystems to include legal systems, programming languages, organizational management, and other code-governed systems.

### 3.6 Institutional Economics and Collective Action

Ostrom’s design principles for long-enduring common-pool resource institutions (Ostrom, 1990, 2005) identify structural features—clear boundaries, low-cost conflict resolution, minimal recognition rights, nested governance—that correlate with institutional survival. In the proposed framework: clear boundaries define the code’s domain; low-cost conflict resolution provides heat-dissipation channels; nested governance establishes multi-layer coding architecture. Ostrom’s empirical finding that systems satisfying 7–8 principles have >85% long-term survival rates, while those satisfying fewer than 3 all collapse (Ostrom, 1990, ch. 3), provides an empirical anchor for the claim that code structure determines system antifragility.

North’s institutional change theory (North, 1990) describes how institutions (codes) reduce uncertainty (specific-dimension entropy decrease) while creating new interest conflicts and strategic spaces (entropy leakage to other dimensions). The proposed theory’s coding-evolution cycle formalizes this dynamic.

The three design conditions derived in §2.9 also map onto Ostrom's principles, which suggests that her empirical regularities may be instances of the framework's derived conditions rather than a separate list. Clear boundaries correspond to a well-specified code domain; low-cost conflict resolution and nested governance correspond to redundancy in routing and to slack in adjustment capacity; the requirement that rules be modifiable by most users corresponds to the presence of a revision channel, which is §2.9's second compliance channel. The mapping is interpretive at present, but it takes a testable form (§6.3).

### 3.7 Complexity Economics

Arthur’s complexity economics (Arthur, 2013, 2021) views markets as non-equilibrium, emergence-driven systems where agents continuously adapt their strategies. Beinhocker (2006) describes economic evolution as a search algorithm operating on a space of “business plans” (codes). The proposed theory aligns with these frameworks but adds a diagnostic dimension: it asks not only how emergence happens, but what kind of emergence is not fragile. It focuses on the dimension distribution of control rather than the fact of emergence itself.

### 3.8 Novel Contributions

While individual components of the theory have precedents, the following elements represent novel synthesis:

1. The unified mechanism of control as compression mapping provides a common language for control operations across physical, biological, social, and institutional domains.

2. The cross-domain generalization of the entropy-leakage principle—that entropy transfer across dimensions, well documented in thermodynamics and ecology, applies with equal structural force to social and institutional systems—offers a testable diagnostic for why optimizing one dimension often degrades overall system health.

3. The causal-hierarchy microfoundation of the coding-evolution cycle, including the factorial-combination argument for why the second beat is unavoidable. This converts the claim that the cycle is universal from a stipulation into a derivation (the earlier versions of this argument rested on the weaker premise that the code-space contains only codes).

4. The identification of three cross-disciplinary fallacy patterns, their correspondence to stallings of the coding-evolution cycle (§4.4), and the division of self-referential closure into interest-based and epistemic types with truth-seeking and interest-defending dispositions, together with the three conditions under which a closure can be opened (§4.5).

5. A redefinition of antifragility as a dimension distribution rather than a scalar quantity, distinct from its use in Taleb (2012), with an explicitly comparative operational form.

6. The control module: the derivation of a unified diagram from selection against control coupling, the two channels of compliance (entropy supply and information coding), and the derivation of three design conditions—redundancy, slack, and fluctuation—from the beats of the coding-evolution cycle.

7. The distinction between material entropy and information entropy, and the consequence that dominance rests on entropy supply rather than control density. This locates the limit of incentive-based coordination without appealing to normative premises.

8. Meta-coding as the structural precondition for revising one's own rules, and the corresponding account of system identity and death as a phase transition in control.

9. The identification of entropy-seeking as a level-specific phenomenon arising from the dissipative flow rather than an independent postulate: the maintenance condition requires intake, selection makes that intake directional, and direction seen from outside is what “entropy-seeking” names. This is offered together with the nested-level scheme (L1–L4) in which evolution's own mechanisms evolve, and with dopamine as the navigational mechanism the selection level requires. The mechanism remains a hypothesis requiring empirical support (§2.7).

10. The explicit complementarity statement with dissipative-structure theory: base completion for the emergence of structure, a difference in subject (birth versus survival and evolution), and one added step—keeping the outlet renewable rather than merely finding it (§3.2).

---

## 4. Cross-Disciplinary Analysis: Three Fallacy Patterns

The theory identifies three structural fallacy patterns that recur across eight disciplines. Each stems from the same root cause: compression mapping as a dimension-specific operation.

### 4.1 Coding Reversal

**Definition:** Each discipline mistakes an operational code for the system’s fundamental purpose. The means of measurement becomes the goal of operation.

**Examples:**

- **Economics:** “Individual utility maximization” is taken as the purpose of markets, when the deeper purpose is maintaining a transaction system that enables continuous code alignment among participants.
- **Political Science:** “One person, one vote” is taken as the purpose of democracy, when the deeper purpose is enabling continuous code evolution in the social system.
- **Medicine:** “Eliminate the pathological target” is taken as the purpose of health, when health is a multi-dimensional entropy balance that requires tracking where intervention-induced entropy leaks.
- **Education:** “Standardized test scores” are taken as the purpose of learning, when learning is the formation of an individual’s own evolutionary engine.

**Mechanism:** Compression mapping is a reduction operation. When a complex multi-dimensional reality is mapped to a single metric (f: all activities → {one number}), the metric becomes the only dimension that “counts.” Over time, the system optimizes for the metric rather than the underlying reality it was designed to proxy.

### 4.2 Dimension Compression Bias

**Definition:** Codes inherently favor measurable dimensions. When “only what is measured gets managed” becomes the default strategy, immeasurable dimensions (buffers, redundancy, empathy, growth) are systematically ignored.

**Examples:**

- **Lean production:** Zero-inventory, just-in-time delivery maximizes efficiency in the measurable dimension of inventory turnover, but eliminates the buffer dimension that absorbs supply-chain shocks. The COVID-19 pandemic revealed the fragility of this optimization (Choi et al., 2023).
- **Scientific evaluation:** Impact factors, citation counts, and publication numbers compress all research activity into countable dimensions. Negative results, replication studies, and paradigm-challenging work—essential for science’s self-correcting mechanism—are filtered out of the “publishable” category.
- **GDP-centered development:** GDP measures the aggregate value of goods and services but remains blind to households on the “poverty knife-edge” (one emergency from destitution), the erosion of social trust, and the depletion of natural capital.

**Mechanism:** This is a structural feature of code-based governance, not a failure of individual cognition. Codes are finite descriptions of control rules; a finite description can only encode a finite number of dimensions. The unencoded dimensions do not disappear. They continue to exist and accumulate entropy, but they lose institutional legitimacy because the system has no language to process them.

### 4.3 Self-Referential Closure

**Definition:** All internal critiques within a discipline are resolved within the existing code framework. Economics adds constraints to utility functions; management replaces bad KPIs with better ones; education responds to the shortcomings of standardization with more standards.

**Examples:**

- **Economics:** Behavioral economics demonstrates that humans deviate from rational-agent assumptions, but the framework remains “deviation from rationality” rather than questioning whether rationality is the right benchmark. Risk management explains post-hoc why lean production was fragile, but cannot diagnose the fragility before a disaster.
- **Political Science:** Arrow’s impossibility theorem proves that no voting system can satisfy all reasonable axioms (Arrow, 1951); public choice theory reveals rent-seeking in voting; deliberative democracy advocates supplement voting with deliberation. All critiques operate within the assumption that voting is the framework; they describe what is lost, but do not question whether the compression mapping itself is the problem.
- **Management:** Goodhart’s Law states that when a measure becomes a target, it ceases to be a good measure (Goodhart, 1975). The response is to design better KPIs, balanced scorecards, and OKRs, all of which remain codes operating in the measurable-dimension space.

**Mechanism:** A discipline’s code framework is also its legitimacy foundation. To question the code is to question the discipline’s basis for existence. Internal critiques therefore converge on improving the code rather than replacing it. This is not intellectual dishonesty; it is a structural property of institutionalized codes.

---

### 4.4 Fallacy Patterns as Stallings of the Cycle

The three patterns describe what goes wrong; the coding-evolution cycle (§2.7) describes how a system stays alive. The two accounts are related, and the relation has practical value: it tells the diagnostician which beat to examine.

Two of the patterns are stallings at a specific beat.

**Coding reversal is third-beat failure.** When a measurement instrument becomes the objective, selection continues to operate, but it no longer filters on the underlying reality—it filters on the reading. Impact factors, KPIs, and growth rates remain live selection pressures; what they select for is conformity to the reading. The third beat has not stopped; it has been disconnected from the environment it is supposed to encode. The remedy is therefore not a better metric but a restored connection between filter and reality: let bad results actually eliminate bad practice.

**Dimension compression bias is second-beat failure.** When codes favor measurable dimensions, unmeasured dimensions lose institutional legitimacy, which is to say they lose the capacity to generate variation. Combination requires material to combine: alternative approaches, heterodox personnel, cross-domain information. A system that has compressed these away still produces new artifacts, but they are permutations of a shrinking code set—recolorings, renamings, repackagings. The second beat does not stop; it is starved. The remedy is not more innovation incentives but restored heterogeneity.

The third pattern is not a stalling at any single beat. Self-referential closure is a meta-level failure: the system's corrective operations remain inside the code framework that produced the problem. It can stall any beat, and, more importantly, it prevents the system from repairing a stall, because repair requires revising the codes, and code revision is the one operation the closure excludes. This is why §4.5 treats it separately, and why the exit condition it requires is structural rather than procedural.

The diagnostic consequence is a two-stage protocol: locate the stalled beat (§5.4), then determine whether the system retains any channel for revising its own codes (§5.6, §2.10). A stalled beat with an open revision channel is a repairable system. A stalled beat inside a closed loop is a system that will keep reporting progress while it loses ground.

### 4.5 Self-Referential Closure: Types and Exit Conditions

**Closure as informational isolation.** Self-referential closure is not merely a failure of effort. It is a structural condition: the system's codes no longer accept correction from signals originating outside them. Stated that way, it has a thermodynamic reading. A dissipative structure persists only while the flow continues (§3.2); a system that stops exchanging with its environment is, in the informational sense, isolated, and the entropy of an isolated system can only increase. Inside such a system, corrective action introduces no new information—it relocates entropy among the dimensions already present. This is why closure resists effort rather than benefiting from it: the operations that would repair the system are drawn from the code that produced the problem, and no operation available inside a closed code space generates a new code.

The consequence for the parent-subsystem relation is immediate. Because every system except the largest is embedded in a parent (§2.5, §2.9), isolation is usually partial and directional: a subsystem stops receiving signals from its parent, or a parent's codes stop admitting signals from its subsystems. Closure is therefore best specified as the failure of the two compliance channels of §2.9—entropy supply and information coding—rather than as a wall around a whole system.

This also clarifies what the exit conditions are. The three conditions below are not a checklist of good practice; they are the stages by which an external signal becomes able to modify a code. A party outside must first be able to place a formulation in front of decision-makers, which opens the downward channel. Someone inside must then concede that the code may be wrong, which is the only event that makes the code itself a candidate explanation, and so opens the upward channel. Finally, internal repair must be exhausted, so that the accumulation of unaddressed entropy is what forces revision—the closed loop demonstrated to be self-insufficient. Interaction with the environment is not a supplement to the repair of a closure; it is the repair.

Self-referential closure admits types, and the type determines prognosis.

**Two axes.** The first axis is the basis of the closure: whether the codes being defended serve the interests of the actors empowered to change them, or whether they have been elevated to unquestionable premises.

- **Interest-based closure.** The actors deciding whether to revise the code are the actors the code benefits. Changing the code means changing their own position, so the available response is to change personnel rather than rules—and the new personnel are selected by the same process that produced the previous ones. Reform is attempted, restructured, and announced; the code is untouched.
- **Epistemic closure.** The code has been promoted to an unquestionable premise, so all diagnoses are forced to locate the problem inside the framework and all remedies are variations within it. Nothing is defended for profit; the framework is simply no longer available for inspection. Diagnosis becomes circular without anyone intending it.

The second axis is the disposition toward external fact: whether the closure can be opened by evidence.

- **Truth-seeking closure.** The core code still contains a commitment that external fact can activate. A discipline whose stated purpose is to find what is true can be wounded by a demonstration that it is not doing so, because the wound is administered by its own stated standard.
- **Interest-defending closure.** Every shock is metabolized as fuel: a scandal becomes a personnel matter, a failure becomes a communication problem, and the code is restated with greater emphasis. No external fact reaches the code, because the code contains no standard to which external fact could appeal.

The distinction is structural rather than moral, and it predicts different trajectories. A truth-seeking closure can be opened; an interest-defending closure cannot be opened from outside and must be superseded.

**Explaining the persistence of failure.** Four mechanisms account for why a closed system continues to report normal operation.

1. **Measurement remains internal.** The signals the system observes are produced by the system. There is no independent instrument, so the readings are consistent regardless of what happens at the productive base.
2. **Feedback is compressed.** Complaints that reach the code are translated into the code's own vocabulary—disloyalty, negativity, insufficient alignment—before they can register as information.
3. **Costs accumulate off-ledger.** Entropy displaced onto unmeasured dimensions is not recorded, so it does not appear as a cost until it manifests as a discrete failure.
4. **The exit is not in the toolbox.** The available corrective instruments are all products of the code, and a tool for replacing the toolbox is, by construction, absent.

**Three conditions for opening a closure.** Because closure is structural, procedural reform does not open it. Three conditions, which must hold jointly, are required.

1. **An outside party with standing knocks.** Objections must arrive not as noise but as a formulation carried by actors with standing sufficient to place it in front of decision-makers. Persistent complaint from parties without standing is absorbed as complaint.
2. **Someone inside concedes the limits of the code.** At least one authoritative actor must publicly concede that the framework may be wrong—that the system does not yet know. This is the narrowest of the three and the one without which the others cannot operate, since it is the only event that makes the code itself a candidate explanation.
3. **Internal repair is exhausted.** Every within-framework adjustment must have been attempted and shown to leave the symptom in place, so that “the rule itself may be the problem” stops being a transgression and becomes the remaining option.

The conditions are individually insufficient and jointly rare, which is consistent with how often systems carry an evidently broken code for decades. They are also conditions on the environment of a system rather than on its internal intelligence: the same competent actors placed in a system lacking one of the three do not escape. This is the framework's clearest statement of an exit condition—the one part of the analysis that specifies what must be present, rather than only what is wrong.

## 5. Diagnostic Protocol

### 5.1 What a Diagnosis Must Produce

A diagnosis is not a list of things that went wrong. It is a judgment about two things: which beat of the coding-evolution cycle has stopped, and whether the system's corrective machinery can still reach the code responsible. Everything in this section serves those two outputs.

The protocol below differs from earlier versions of this framework, and the difference is worth stating plainly. Earlier formulations illustrated system-level diagnosis with a quality-management cycle (Plan-Do-Check-Act) and with the traditional-medicine practice of inferring internal imbalance from surface signs, and treated both as models for how a system should be diagnosed. Neither survives contact with application. Both are operational postures rather than diagnostic instruments: the first tells you how to iterate once a dimension has already been chosen; the second asserts that surface readings carry system-level information. Neither produces the judgment a diagnosis needs, and in applied work neither was used. What was used, repeatedly and across unrelated domains, was a small set of operations—restate the question, fix the boundary, inventory control, trace where the displaced entropy lands, locate the code that drives the rest, locate the stalled beat, test for closure, test whether any door is still open. The protocol below is those operations, in the order in which they were actually performed.

The sequence is not rigid. A case in which the root code is itself the reward structure can move directly from the boundary to the closure test and skip the entropy-flow map, because the conservation step is already implied. But the two outputs named above must be produced in every case, and each of the steps below answers part of that requirement.

### 5.2 Step One: Replace the Question, and Fix the Boundary

The first move in an applied diagnosis is almost never to answer the question as posed. The question as posed is usually the one the system has already asked itself, which is why its framing is part of the problem.

Applied cases begin by replacing it. “Why is the company discriminating by age?” becomes “what is the engine, and is it still running?” “Is the drug inferior?” becomes “who decides which drug a patient receives?” “Are middle-aged researchers less creative?” becomes “how long does it take to reach the frontier of an expanding body of knowledge?” “Is the voting mechanism good?” becomes “what happens to a society's codes when selection is replaced by counting?” The replacement is not a rhetorical device. It is the operational form of the suspicion that the given frame is itself a compression mapping, and the diagnosis will inherit the frame's blind spots if the replacement is skipped.

Where an event spans levels, the boundary is fixed before anything is measured: which parent system, which subsystems, and how many diagrams apply at once. A subsystem can be governed by its organizational diagram, its national diagram, and a supranational diagram simultaneously, and a diagnosis that does not say which one is binding will misplace the remedy. The output of this step is the diagnosis question itself, plus a boundary diagram listing the parent system, the subsystems, and the number of applicable diagrams.

### 5.3 Step Two: Map Control, Trace the Entropy

Two inventory operations follow.

**Inventory the controls.** Which dimensions are actually constrained, in writing and by tacit agreement? Formal instruments count: procurement rules, quarterly reporting, performance categories. Unnamed ones count as well: who may speak last in a meeting, how quickly messages must be answered, which numbers travel upward. The purpose is a control distribution map—where the lines are drawn and how tight they are—because a system's constraints decide what counts as normal before any judgment is passed on it.

**Trace the entropy.** For each compressed dimension, where has the displaced randomness gone? The receiver is usually a dimension that neither reports nor complains, only accumulates. The output is an entropy-flow map: what is compressed, which neighboring dimension is absorbing the cost, and which of those neighbors will reach its limit first. This is the step that converts a plausible grievance into a diagnosis. That the price of a drug fell is a fact; that the difference is being paid in efficacy, in the patient's range of choice, and in the prescriber's ability to judge is a diagnosis.

Where a receiver's remaining margin can be measured, it should be measured. A budget of one percent of member-state GDP, twelve thousand names on a sanctions list, antibody production halved—figures of this kind do not make the framework quantitative, but they fix how far the absorbing dimension is from its ceiling.

### 5.4 Step Three: Locate the Stalled Beat

The cycle is collision, combination, selection: reality produces a situation the existing codes cannot handle; the failure produces a new code; new and old codes recombine into more variation than any controller can enumerate; the environment filters the results, and what survives becomes the starting point of the next round. A system stops evolving when one of the three stops, and each presents a recognizable symptom.

- **Collision has stopped.** Symptoms: nobody proposes anything; post-mortems are ceremonial; errors occur without becoming anyone's experience. The people who knew how the pit was dug have left, and what remains is execution. The remedy is to restore the raw material of collision—room for failure, review with teeth, and authority for the people nearest the work to change it on the spot.
- **Combination has withered.** Symptoms: output continues, but each new artifact is a permutation of the existing code set—recolored, renamed, repackaged. Heterogeneity has been compressed away, and with it the material of recombination. The remedy is to restore heterogeneity: different origins, different information channels, methods imported from other industries, at the cost of more friction in the short run.
- **Selection has been disconnected.** Symptoms: bad practice does not die. Selection still operates, but it filters on the quality of reporting rather than the quality of the work. The remedy is to return selection to reality: let adverse results be visible, let bad outcomes eliminate bad practice, and let the report reconcile with the floor.

This step is the center of the protocol, and it is what distinguishes the framework from a general account of incentives or a standard risk model. Neither of those tells you which of the three has stopped, and the three take different remedies.

### 5.5 Step Four: Find the Root Code and the Leverage Level

Locating the stalled beat says what is wrong with the system. It does not say who can change it. In nested systems the two are separated by the code chain.

Following the chain upward identifies the root code: the code that drives the level below it and is not directly punished by the level above. A quarterly reporting cadence driving a cost program driving the departure of the people who carried institutional knowledge. An evaluation metric driving a management style that the metric was never designed to constrain, sustained because the actors who would revise the metric were selected by it. Two stated premises about how a political system succeeds, driving the diagnostic framework into which all subsequent analysis is forced. The root code is characterized by insulation: nothing above it corrects it.

Following the chain downward traces where each level's compression sends its entropy, and whether that entropy dissipates or accumulates by the end of the chain. Reading the two directions together identifies the leverage level—the level at which a code change is not punished by a higher level. Intervention below that level is absorbed; intervention above it is not available.

### 5.6 Step Five: Test for Closure, and Test the Doors

A stalled beat is repairable if the system retains a channel for revising its codes. Three questions detect the absence of one. First, do corrective operations fall inside the code framework or outside it—new personnel, finer metrics, an internal review, or something that touches the code itself? Second, who defines the problem and who supplies the remedy: are they the parties the code as it stands benefits? Third, does the core code still contain a standard to which external fact can appeal, or is every shock metabolized as confirmation?

On these questions the types of §4.5 separate, and the type determines the prognosis. An interest-based closure changes personnel and not rules, because the actors who would revise the rule are the actors the rule positions. An epistemic closure forces every diagnosis into a frame that is no longer available for inspection. A closure whose core code still contains a truth commitment can be wounded by its own standard; one that does not will restate the code with greater emphasis and continue.

The final test is whether any door remains open—which is not the same as asking whether the current metrics look healthy. Can anyone still say that the direction may be wrong? Does unarranged collision still occur? Is an eccentric proposal received, or dismissed for not producing numbers? Applied work gives the test two forms. The weaker form asks whether an information-entropy channel exists at all: a subsystem whose code does not align with the parent's has no channel, only a wall, and the parent's diagram will not survive on that basis. The stronger form—used in the one case where a closure was actually opened—asks whether the three conditions of §4.5 hold at once. Where they do, the code becomes available for revision. Where any one is missing, the same competent actors will do what the structure permits, which is to keep reporting progress.

### 5.7 Step Six (Conditional): Supplementary Instruments

Four instruments appear in applied work, each suited to a condition.

- **Comparison cases.** A second system with the same mechanism and a different outcome separates structure from fate. Where the mechanism is present and the outcome differs, the mechanism is not destiny. This is the cheapest available test that a diagnosis has identified a structure rather than a local grievance.
- **Measurement of margins.** Where the absorbing dimension can be measured, quantify it (§5.3). The figure does not make the framework quantitative, but it fixes the distance to the ceiling.
- **External probes.** An observer whose incentives do not depend on the code's stability will detect in hours what the system has not detected in decades. The probe localizes the blind spot and indicates whether the closure has cracked.
- **Inference before observation.** For systems too large or too slow to observe directly, derive the predicted failure modes from the framework first, then check the record. This is the closest the present framework comes to a test (§6.2).

### 5.8 From Diagnosis to Remedy

The remedy is selected by the stalled beat, not by the symptom: restore collision, restore heterogeneity, or restore selection. Two rules constrain how it is applied.

**The lever must not be another compression mapping.** Replacing metric X with metric Y, or repairing the damage a metric caused by measuring that metric more precisely, applies a new constraint to the same problem. It does not restart the cycle; it relocates the compression. The test is mechanical: state which dimension the proposed remedy compresses, and where that compression's entropy will land. In applied cases the test was decisive more than once. Directing firms to optimize for long-run value commits the same error the capital market commits, one level up. Catching more fraud by writing stricter screening rules adds compression to a system whose problem is excessive compression. Reframing reimbursement so that the insurer pays a basic price and stops determining which drug the patient receives withdraws a control rather than adding one, and that case is the clearest instance of a remedy that restarted something.

**The lever is the reward and penalty structure.** Short-horizon behavior must stop being free, long-horizon accumulation must become visible, and the cost of entropy leakage must fall on the party that released it. The framework does not produce a correct code. What it can do is identify which structure is currently paying for what, and change that.

Where the diagnosis found a closure, the remedy is not inside the stalled beat. The three conditions of §4.5 describe what must become true before the code itself can be revised, and they are conditions on a system's environment rather than on its intelligence. What an actor inside the closure can do is limited to the first step, which is to see the loop: to recognize that the available options were generated by the code that produced the problem, and that a tool for replacing the toolbox is, by construction, absent from it.

---

## 6. Discussion

### 6.1 What This Theory Provides

The theory does not supply a “correct code” to replace all others; that would itself commit coding reversal. Instead, it provides three tools:

1. **Dimension diagnosis before code operation.** Before any measurement or optimization, the framework asks: What are this system’s core survival dimensions? Which are covered by existing codes, and which are neglected? Under what conditions will entropy leakage from neglected dimensions breach critical thresholds?

2. **Codes as evolution objects, not a priori frameworks.** A discipline’s current core codes—utility functions, GDP, blood-pressure standards, admission scores—are historical products, not cosmic constants. They should iterate with system-state changes. In practice, codes acquire institutional inertia because changing them means changing the discipline’s legitimacy foundation.

3. **Antifragility as a cross-disciplinary meta-standard.** The test of a theory or practice is not what it measures, predicts, or controls, but whether it can maintain core functions under unexpected shocks and obtain structured improvement from those shocks.

### 6.2 Limitations

The theory, in its current form, has several significant limitations:

1. **Qualitative nature.** The framework provides conceptual direction but lacks formalized mathematical definitions, measurement protocols, and quantitative predictions. The claim that entropy leaks from dimension A to dimension B cannot currently be operationalized with specific units or thresholds.

2. **No prospective predictive record.** The diagnostic claims—for example, that a system with compression mapping applied to its dissipation dimensions will collapse—have not been tested in a prospective, falsifiable study. The case analyses assembled so far are retrospective, with one partial exception: an inference-first analysis of a multi-level governance system that derived five predictions from the framework before examining the record, and found the predicted failure modes in four subsequent crises. That is closer to an internal consistency test than to prospective validation, and it is the only such case.

3. **Scope ambiguity.** The theory claims to cover physics, biology, and social systems under one framework, but the concept of “entropy” operates at different levels of abstraction in each domain. The bridging argument—that the mathematical structure is isomorphic across domains—has not been formally demonstrated.

4. **No empirical calibration.** Unlike Ostrom’s design principles (tested against 91+ case studies) or ecological resilience theory (which has identified measurable regime-shift thresholds), the theory has not been calibrated against empirical data.

5. **No priority rule for the normative use of antifragility.** Antifragility is proposed as a cross-disciplinary meta-standard (§6.1), but the framework does not currently specify how to adjudicate cases in which raising the antifragility of one system lowers that of another—for instance, when an action increases the antifragility of a group while decreasing that of the larger system containing it. A priority ordering over nested systems, or a principle allocating entropy rights, is required. This is a gap in the framework rather than an error, and it is load-bearing for any applied use.

6. **Terminology risk.** In the social register, “entropy” is a heuristic rather than a measured quantity (§2.7). A reader who imports the thermodynamic reading will misjudge the framework's claims in both directions, treating heuristic statements as if they carried units, or dismissing structural claims for want of them.

### 6.3 Path to Formalization

The most promising path to formalization builds on three empirical anchors in the literature:

- **Ecological resilience theory** (Holling, Gunderson) provides measurable “controlling variables”—the slow variables that determine system behavior, which are the ecological equivalent of the theory’s “dimensions.” Documented regime shifts—for example, the shift from clear-water to turbid states in shallow lakes (Scheffer et al., 2001), coral reef degradation, and rangeland desertification—provide measurable thresholds corresponding to the theory’s “entropy-leakage critical points.” More recent work generalizing Ashby’s law to multi-scale systems (Siegenfeld & Bar-Yam, 2025) suggests a formal pathway for extending requisite-variety reasoning across hierarchical levels.

- **Ostrom’s design principles** (Ostrom, 1990) provide an operationalized checklist of code-structure properties that correlate with institutional survival. These may be reinterpreted as “code antifragility indicators” and tested against the theory’s predictions.

- **Innis and McLuhan’s media theory** (Innis, 1951; McLuhan, 1964) provides a generative mechanism for why codes become self-locking: the physical structure of the code medium biases what content is easily produced, transmitted, and institutionalized. This explains the mechanism behind dimension-compression bias.

A formalization program could proceed by (1) defining a multi-dimensional state space for a target system; (2) operationalizing compression mapping as variance reduction in selected dimensions; (3) defining antifragility as a comparative property, with a scalar summary—the probability of maintaining core function under a specified shock distribution—as a derived convenience rather than a definition; and (4) testing the prediction that compression applied to dissipation dimensions reduces antifragility more than equivalent compression applied to control dimensions.

Three further implications of §2.6 and §2.9 are testable without waiting for a full formalism. First, if the second beat of the cycle is unavoidable once codes exist, then the ratio of novel to repeated code combinations should decline as the effective code set contracts, and should recover when the code set is enlarged by external inputs. Second, if redundancy, slack, and fluctuation are the conditions under which the cycle continues, then systems whose diagrams lack them—single-route dependencies, entropy supply tuned to exact current need, uniform supply intensity—should show lower survival under matched shocks than systems that retain them. Third, if self-referential closure requires the joint presence of three conditions to open (§4.5), then cases in which a system did revise its core code should exhibit an outside actor with standing, a public concession of ignorance by an authoritative insider, and an exhausted internal repair sequence; cases with only two of the three should not have reopened.

A minimal prospective test of the framework could take the following form. Identify a system currently undergoing compression in a measurable dimension—for instance, a regulatory tightening that constrains a specific industry practice. Using the protocol of §5, predict which adjacent dimension is most likely to absorb the displaced entropy (for instance, informal compliance workarounds, unreported risk externalization, or deterioration in an adjacent service quality), and predict which beat of the cycle will be reported as healthy while failing (for instance, continued output of nominally new artifacts that are permutations of an unchanged code set). Specify observable indicators that would confirm the predictions and indicators that would disconfirm them. A single such study—predicting leakage and the stalled beat before they are observed, rather than explaining them post-hoc—would move the framework from retrospective coherence to testable hypothesis.

### 6.4 Complementarity with Traditional Science

The theory’s relationship to traditional science is one of complementarity, not replacement. In domains where control is deep and entropy leakage is minimal—particle physics, orbital mechanics, chemical kinetics—state-derivation methods are highly effective. The theory predicts and explains this: when control is near-complete and leakage is near-zero, risk assessment and state derivation should, in principle, yield equivalent conclusions. In domains where control is shallow and leakage is high—social systems, organizational design, economic policy—state-derivation methods systematically fail because they do not track entropy transfer across unmodeled dimensions. The theory provides a complementary diagnostic tool for these domains.

---

## 7. Conclusion

This paper began by redefining a foundational concept: control is not the achievement of a target state but the ongoing process of transporting randomness across dimensions. This redefinition makes entropy the natural language of control, reveals antifragility as an independent property rather than a blend of rigidity and flexibility, and—through the introduction of coding—transforms the study of system evolution from a collection of domain-specific narratives into a unified analytical framework.

The theory identifies three cross-disciplinary fallacy patterns—coding reversal, dimension compression bias, and self-referential closure—that recur across eight disciplines. These patterns are structural consequences of code-based governance rather than the result of individual cognitive bias, and they are not an unrelated list. Reversal and compression bias are the third and second beats of the coding-evolution cycle failing respectively; closure is a meta-level failure that prevents repair of either. Read this way, the fallacy catalogue is a diagnostic index into a single mechanism.

The mechanism itself no longer rests on a stipulation. The causal hierarchy (§2.6) supplies its microfoundation: intervention is entropy decrease in a dimension, counterfactual combination is entropy increase over codes, and once codes exist the combinatorial space is factorial in their number, so no controller can cover it. That is why the cycle turns. It also fixes the division of labor with the traditions the framework draws on: dissipative-structure theory supplies the base—how randomness organizes into structure—while this framework addresses what happens afterward, when a structure must keep its outlets open and its outlets renewable (§3.2).

**The closed loop: evolution as the foundation of stability.** The most consequential result of treating evolution as a system is the argument that a system's capacity to evolve is not a secondary consideration; it is the precondition for stability itself. A system that cannot evolve cannot sustain its structure under the entropy leakage produced by its own operations. The accumulation of entropy in unmanaged dimensions guarantees eventual collapse unless the system can modify its codes—that is, evolve. Stability is therefore not a property that can be designed once and preserved; it must be continuously regenerated through evolutionary motion.

Two further consequences follow from treating the parent-subsystem relation explicitly. First, coordination has two independent channels, and only one of them is bounded. Material entropy has a ceiling set by productive capacity, and a system that relies on it alone has compliance that fluctuates with that ceiling. Information entropy generated through shared codes has no comparable ceiling, which is why long-term viability in this framework means that information-entropy supply covers the troughs of material-entropy fluctuation (§2.9). Second, since dominance rests on entropy supply rather than control density, the framework's central prescription is not a prescription for more control or less, but for a dimension distribution that leaves the cycle with room to turn—expressed as three derived obligations: redundancy across routes, slack in supply, and fluctuation in intensity.

A third consequence is more general. Antifragility is acquired through exchange with the environment and with the parent system, not designed from within (§2.9). Isolation—whether emergent, as in a self-referential closure, or deliberate, as in the compression of dissipation dimensions—does not merely slow a system down. It lowers the ceiling on the antifragility the system can ever possess, and the loss stays invisible until a shock exceeds the new ceiling.

The diagnostic language this theory provides—compression mapping, entropy leakage, dissipation bandwidth, dimension distribution, stalled beat—is ultimately a language for assessing whether a system's evolutionary capacity is keeping pace with its entropy production, and whether its remaining corrective operations can reach the codes that generated the problem.

The theory is currently qualitative. Its next steps involve operationalizing compression mapping, entropy leakage, and antifragility within measurable multi-dimensional state spaces, and testing the predictions stated in §6.3: that systems with insufficient evolutionary bandwidth deteriorate even when their momentary control metrics appear healthy, that systems lacking redundancy, slack, or fluctuation survive matched shocks less well, and that a self-referential closure reopens only when all three of its exit conditions are present. Until formalized, the theory offers a diagnostic coherence that no single-discipline framework provides: a common language for reasoning about which dimensions need control, which need release, and whether a system's evolutionary engine is running fast enough to outrun its own entropy.

---

## References

1. Arrow, K. J. (1951). *Social Choice and Individual Values*. Wiley.
2. Arthur, W. B. (2013). *Complexity Economics: A Different Framework for Economic Thought*. SFI Working Paper.
3. Arthur, W. B. (2021). Foundations of complexity economics. *Nature Reviews Physics*, 3, 136–145.
4. Ashby, W. R. (1956). *An Introduction to Cybernetics*. Chapman & Hall.
5. Beer, S. (1972). *Brain of the Firm*. Allen Lane.
6. Beer, S. (1979). *The Heart of Enterprise*. Wiley.
7. Beinhocker, E. D. (2006). *The Origin of Wealth*. Harvard Business School Press.
8. Boltzmann, L. (1877). Über die Beziehung zwischen dem zweiten Hauptsatze der mechanischen Wärmetheorie und der Wahrscheinlichkeitsrechnung. *Wiener Berichte*, 76, 373–435.
9. Choi, T. Y., Netland, T. H., Sanders, N., Sodhi, M. S., & Wagner, S. M. (2023). Just-in-time for supply chains in turbulent times. *Production and Operations Management*, 32(7), 2331–2340.
10. Gibbs, J. W. (1878). On the equilibrium of heterogeneous substances. *Transactions of the Connecticut Academy of Arts and Sciences*, 3, 108–248, 343–524.
11. Goodhart, C. (1975). Problems of monetary management: The U.K. experience. *Papers in Monetary Economics*, 1, 1–20.
12. Gunderson, L. H., & Holling, C. S. (Eds.). (2002). *Panarchy: Understanding Transformations in Human and Natural Systems*. Island Press.
13. Holling, C. S. (1973). Resilience and stability of ecological systems. *Annual Review of Ecology and Systematics*, 4, 1–23.
14. Innis, H. A. (1951). *The Bias of Communication*. University of Toronto Press.
15. McLuhan, M. (1964). *Understanding Media: The Extensions of Man*. McGraw-Hill.
16. Nicolis, G., & Prigogine, I. (1977). *Self-Organization in Nonequilibrium Systems: From Dissipative Structures to Order through Fluctuations*. Wiley.
17. North, D. C. (1990). *Institutions, Institutional Change and Economic Performance*. Cambridge University Press.
18. Ostrom, E. (1990). *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press.
19. Ostrom, E. (2005). *Understanding Institutional Diversity*. Princeton University Press.
20. Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press.
21. Pearl, J., & Mackenzie, D. (2018). *The Book of Why: The New Science of Cause and Effect*. Basic Books.
22. Prigogine, I., & Stengers, I. (1984). *Order out of Chaos: Man’s New Dialogue with Nature*. Bantam Books.
23. Scheffer, M., Carpenter, S., Foley, J. A., Folke, C., & Walker, B. (2001). Catastrophic shifts in ecosystems. *Nature*, 413(6856), 591–596.
24. Schrödinger, E. (1944). *What is Life?* Cambridge University Press.
25. Schultz, W. (1998). Predictive reward signal of dopamine neurons. *Journal of Neurophysiology*, 80(1), 1–27.
26. Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27, 379–423, 623–656.
27. Siegenfeld, A. F., & Bar-Yam, Y. (2025). A formal definition of scale-dependent complexity and the multi-scale law of requisite variety. *Entropy*, 27(8), 835.
28. Taleb, N. N. (2012). *Antifragile: Things That Gain from Disorder*. Random House.
29. Wiener, N. (1948). *Cybernetics: Or Control and Communication in the Animal and the Machine*. MIT Press.
30. Wittgenstein, L. (1922). *Tractatus Logico-Philosophicus*. (C. K. Ogden, Trans.). Routledge & Kegan Paul.

---

*This white paper is released under CC BY-NC-SA 4.0. First published 2026-05-25. For discussions, please open an issue at the project repository.*
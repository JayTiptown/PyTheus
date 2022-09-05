### config files

The config file collects all information necessary for setting up and running the optimization as well as for saving the
results to a file. The content of the config file is saved into the same directory as the results produced by its run.
Automatically keeping track of all optimization settings allows users to reproduce results more easily.

#### keywords of config files

`description` Description of the experiment that the optimization aims to discover. Is printed at the start of the run.

`foldername` Name of the subfolder. By default, files are saved in _output/configfilename/foldername_. When name is taken, numbers are added.

`samples` Number of optimizations done.

`loss_func` Loss function used. Check _loss_dic_ in _theseus.lossfunctions.py_ for values.

`thresholds` In each optimization step, the loss functions have to be below the thresholds to be considered successful. 

`target_state` Target state for state creation, logic table for quantum gates.

`amplitudes` amplitudes of the kets in the target states. If not given all amplitudes are set to one.

`num_anc` Number of ancillas.

`unicolor` Starting graph is restricted to have only mono-colored edges between target nodes. Less edges mean faster optimization, but it can be a gamble. If your solution is not possible without two-colored edges between target nodes (such as ghz_346) it will not be found.

`removed_connections` list of connections that are removed from complete starting graph before optimization. Can be applied e.g. for entanglement swapping. 

`single_emitters` Defines nodes corresponding to single emitters. Automatically introduces constraints on connections in starting graph (no connections to other single_emitters or in_nodes).

`in_nodes` Defines nodes corresponding to incoming particles, e.g. for measurements and gates. Automatically introduces constraints on connections in starting graph (no connections to other in_nodes or single_emitters).

`out_nodes` Defines nodes corresponding to outgoing particles that are not measured, e.g. for heralded state creation and heralded gates.

`heralding_out` set to true means that `out_nodes` are not detected.

`novac` set to true means that heralded `out_nodes` are guaranteed, no vacuum.

`imaginary` Set false for real number optimization. Set to 'polar' for complex number optimization in polar format.

`optimizer` Optimizer used by scipy.optimize.minimize

`ftol` convergence tolerance for scipy.optimize.minimize

`num_pre` Number of preoptimization done before starting topological optimization on the best result. For target state optimization 1 is good. For entanglement optimization higher values can be better.

`bulk_thr` After preoptimization some edge weights can already be very small. Setting this value to e.g. 0.01 will delete all edges that have a weight smaller than this in absolute value. This can save a lot of time for very big starting graphs, where optimization of many parameters is slow. To skip this step set value to 0.

`topopt` defines if topological optimization is performed. If not given, default value is true. If false, no topological optimization is done (bulk_thr is also overwritten to 0).

`tries_per_edge` During topological optimization, this value sets how often optimization is attempted after deleting one edge. If all tries fail, the next smallest edge is attempted.

`edges_tried` During topological optimization, this value sets how many of the smallest edges are attempted to be deleted. If the optimizer fails to delete all of these edges, topological optimization is terminated.

`safe_hist` If set to true, the history of the loss function values for each topological optimization step is tracked and saved into the result file.

#### for loss_func = 'ent'

`K` 

`dim` Vector defining local dimensions

`min_edge`

`var_factor`

## Naming Conventions for config files
#### Gates
* postselected: `_post`
* single photon sources: `_sp`
* target photon starts in mode 0: `_0`

#### GHZ States
The file `ghz_346` is for a `3` particle `4` dimensional GHZ state produced with a total of `6` photons (in this case this means that 3 ancilla photons are used)

#### Condensed Matter States
File name ending in `_n` identifies that the `n` particle version of that state is produced.


# The List

✅✅ ... found and saved in configs, counted as list contribution

✅🤔 ... exists but config not ready

🤔 ... not found (not sure if it works)

### GHZ

* 3 particle, 4 dimension ✅✅
* 3 particle, 5 dimension ✅✅
* 3 particle, 6 dimension ✅✅
* 4 particle, 4 dimension ("fake") ✅✅
* 4 particle, 4 dimension (HALO)
* 5 particle, 4 dimension ✅✅
* 6 particle, 3 dimension (HALO)

### Quantum Info

* BSSB4 state (real and complex versions) ✅✅
* ~~Psi5~~ BSSB5 state ✅✅
* Cluster states
    * 4 particle ✅✅
    * 5 particle ✅✅
    * 6 particle ✅✅
* random matrix state 1 (3 qubits) ✅✅
* random matrix state 2 (3 qubits) ✅✅
* symmetric state
    * 3 particle, 3 dimension ✅✅
    * 4 particle, 3 dimension ✅✅
    * 5 particle, 2 dimension ✅✅
    * 6 particle, 2 dimension (rough, but no anc) ✅✅
* Schmidt rank vector
    * (5,5,4) ✅✅
    * (6,3,2) ✅✅
    * (6,5,5) ✅✅
    * (7,3,3) ✅✅
* W state x W state ✅✅
* Steane Code (rough) ✅✅
* Shor Code ✅✅
* Hyperdeterminant State ✅✅
* L state ✅✅
* Yeo Chua state ✅✅
* 9 entanglements in 4 qubits
    * La4 (with real amplitudes) ✅✅
    * L053 ✅✅
    * L071 ✅✅
    * Other trivial states (stored, but they do not count)
* Bell gem
    * 4 particles ✅✅
    * 8 particles 🤔

### k-uniform and AME states

* 4 qubit real coefficients ✅✅
* 4 qubit complex coefficients (Higuchi Sudbery)  ✅✅
* 5 particle, 2 dimension AME ✅✅
* 6 particle, 2 dimension AME ("fake")  ✅✅
* 6 particle, 2 dimension, k=2 uniform ✅✅
* dim = (3,3,3,1) (GHZ state)
* 4 particle, 3 dimension, k=2 uniform ✅✅
* 7 particle, 2 dimension, 'almost' k=2 ✅✅
* 8 particle, 2 dimension, 'almost' k=3 ✅✅

### Mixed States

* Werner State ✅✅
* Peres State (fake) ✅✅
* more ?

### Measurements / Quantum Comm

* GHZ analyzer
    * 3 particle, 2 dimension ✅✅
    * 3 particle, 3 dimension ✅✅
    * 3 particle, 4 dimension ✅✅
* Mean King
    * 2d ✅✅
    * 3d ✅✅
    * 4d 🤔
* W analyzer ✅✅
* HS analyzer ✅✅
* 4d Entanglement swapping (HALO)
* 3 particle entanglement swapping ✅✅
* 2 particle, 3 dimensional entanglement swapping ✅✅

### Gates

* CNOT(2,2) (known)
* CNOT(2,3) heralded by 2 ancillas ✅✅
* CNOT(2,3) postselected with 2 ancillas ✅✅
* CNOT(2,4) postselected with 2 ancillas ✅✅
* CNOT(3,3) postselected with 2 ancillas ✅✅
* Toffoli postselected without ancillas ✅✅
* Fredkin postselected with 2 ancillas ✅✅
* CNOT(3,3) on 0 ✅🤔
* CNOT(4,4) on 0 ✅✅
* Toffoli ✅🤔
* Toffoli on 0 ✅🤔
* controlled Z with 4 ancillas ✅✅
* controlled Z postselected with 2 ancillas ✅✅
* Fredkin on 0 ✅🤔
* more ?

### Single Photon Sources as a Resource

* GHZ 4 particle, 3 dimension, 2 single photon sources, 2 ancilla ✅✅
* GHZ 4 particle, 3 dimension, 6 single photon sources ✅✅
* W states
    * 3 particle ✅✅
    * 4 particle ✅✅
    * 5 particle ✅✅
* CNOT(2,2) with two single photon sources ✅✅ (different from known experiment, better successrate?)
* CNOT(2,3) postselected with three single photon sources ✅✅
* CNOT(3,3) postselected with four single photon sources ✅✅
* Fredkin postselected with one single photon source ✅✅
* controlled Z with three single photon sources ✅✅
* controlled Z postselected with one single photon source ✅✅
* 3d Entanglement Swapping with single photon sources ✅✅ 

### Condensed Matter

* AKLT spin 1
    * 3 particle ✅✅
    * 4 particle 🤔
* AKLT spin 2
    * 3 particle 🤔
    * 4 particle 🤔
* Haldane states
    * 3 particle A 🤔
    * 3 particle B ✅✅
    * 3 particle C ✅✅
* Majumdar Gosh states
    * 4 particle ✅✅
    * 6 particle ✅✅
* N body
    * 3 particle ✅✅
    * 4 particle ✅✅
    * 5 particle ✅✅
    * 6 particle ✅✅
* weak Antiferrometric
    * 1 - 3 particle ~~(rough)~~ ✅✅
    * 2 - 3 particle ~~(rough)~~ ✅✅
    * 3 - 3 particle ✅✅
    * 4 - 3 particle ✅✅
* 3 particle spin3- ✅✅
* 3 particle spin3+ (same than previous, only color changes)
* 4 particle spin half ✅✅
* 3 particle spin1 ~~("fake")~~ ✅✅
* 1d spin half wire ✅✅

### Other

* 4 qubit state that needs complex numbers ✅✅

### Fock States
* Noon 2 modes 2 particles (not new, but pedagogic)
* Noon 2 modes 3 particles (new?)
* Noon 3 modes 3 particles (can it be generalized?) ✅✅
* Tetrahedron 40+13 (different coefs) ✅✅
* Cube 80+44+08 ✅✅
* Octahedron, either 04-40 or 51-15
    * fake with 2 ancillas ✅✅
    * honest with 4 ancillas ✅✅
    * check 40+04 from xuemei

### More ideas/inspiration

* maximize properties of mixed states
* graph theoretical properties, assembly index, etc.
* optimize quantum info inequalities (similar to CHSH)
* maximize robustness (similar to HS state)
* GKP states
* Heralded states
* experiments with interesting restrictions

```python

```

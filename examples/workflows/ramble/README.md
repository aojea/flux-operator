# Ramble

Let's test [ramble](https://github.com/GoogleCloudPlatform/ramble)
in the Flux operator. This is just a hello world experiment that runs
the hostname. I did test gromacs but hit segfaults and ran away (the workspace
is in the container for anyone interested)!

> I would recommend this for groups that are already using spack for running workflows (e.g., spack environments)
> I would not recommend ramble if you are starting fresh and have a choice of what tools to use.
> Either way, I recommend that you try it out. I like the idea of having recipes for reproducible workflows, conceptually.

## Usage

First, let's create a kind cluster. From the context of this directory:

```bash
$ kind create cluster --config ../../kind-config.yaml
```

And then install the operator, create the namespace, and apply the MiniCluster YAML here.

```bash
$ kubectl apply -f ../../dist/flux-operator.yaml
$ kubectl create namespace flux-operator
$ kubectl apply -f ./minicluster.yaml
```

This will create the MiniCluster, and you can wait for the pods to be running (it took over 7 minutes for me)!
Then look at the logs to see ramble run:

```bash
==>     Executing phase get_inputs
==>     Executing phase make_experiments
==>     Executing phase get_inputs
==>     Executing phase make_experiments
==> Warning: The env-vars workspace section is deprecated. Environment variables
==>     Executing phase get_inputs
should be defined in the env_vars config section using the same
==>     Executing phase make_experiments
syntax. Support for env-vars will be removed in a future. See
==>     Executing phase get_inputs
the documentation for examples of the new syntax.
==>     Executing phase make_experiments
flux-sample-1
0.00user 0.00system 0:00.00elapsed 0%CPU (0avgtext+0avgdata 1380maxresident)k
0inputs+0outputs (0major+70minor)pagefaults 0swaps
flux-sample-3
0.00user 0.00system 0:00.00elapsed 0%CPU (0avgtext+0avgdata 1484maxresident)k
0inputs+0outputs (0major+71minor)pagefaults 0swaps
flux-sample-2
0.00user 0.00system 0:00.00elapsed 0%CPU (0avgtext+0avgdata 1432maxresident)k
0inputs+0outputs (0major+72minor)pagefaults 0swaps
flux-sample-0
0.00user 0.00system 0:00.00elapsed 0%CPU (0avgtext+0avgdata 1432maxresident)k
```

A warning that the above produces segfaults / errors for me, even for just hostname,
which is a fairly big red flag (and I'm not sure why). I would recommend ramble for groups
that are already using Spack and want to put some structure and reproducibility to their workflows,
but would not recommend it for starting out fresh.  If you want to extend this example, you can work
from the Dockerfile build [here](https://github.com/rse-ops/flux-hpc/blob/main/ramble-gromacs/Dockerfile)
to prepare a custom container. If you want to debug something, you can set interactive: true to run in interactive mode, and then shell into the pod, connect to the broker:

```bash
$ kubectl exec -it -n flux-operator flux-sample-0-jlsp6 bash
$ sudo -u flux -E $(env) -E HOME=/home/flux flux proxy local:///run/flux/local bash
```

And when you are done, clean up:

```bash
$ kubectl delete -f minicluster.yaml
```


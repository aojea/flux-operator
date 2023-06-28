# Testing Faux Child Broker

Create the minicluster (and install the flux operator)

```bash
$ kind create cluster --config ../../machine-learning/kind-config.yaml
$ kubectl create namespace flux-operator
$ kubectl apply -f ../../dist/flux-operator.yaml
$ kubectl apply -f minicluster.yaml
```

Shell in:

```bash
$ kubectl exec -it -n flux-operator flux-sample-0-ldwph bash

# connect to the broker
$ sudo -u flux -E $(env) -E HOME=/home/flux flux proxy local:///var/run/flux/local bash
```

Note that we are installing bc, so if you get an error it can't connect just wait because
that is likely still running. Next, note the resources we have from the index 0:

```bash
$ flux resource list
```
```
$ flux resource list
     STATE NNODES   NCORES    NGPUS NODELIST
      free      4       16        0 flux-sample-[0-3]
 allocated      0        0        0 
      down      0        0        0 
```

Each of the following examples should be run from the root node for the time being.
You'll want to change directory to `/tmp/workflow`:

```bash
$ cd /tmp/workflow
```

## Instance 1 node smaller

Let's first create an allocation we know will work, asking for 1 fewer nodes! This will
use the assets in [1-smaller](1-smaller).


```bash
$ flux alloc --conf ./1-smaller/broker.toml -N 3 bash
```

This should work! Note the new resources:

```bash
$ flux resource list
     STATE NNODES   NCORES    NGPUS NODELIST
      free      3       12        0 flux-sample-[1-3]
 allocated      0        0        0 
      down      0        0        0 
```

## Instance larger

Let's make an arbitrary sized "burst" and ask to run hostname on it. This likely isn't perfect,
but is just emulating what we might do. I'm going to use a batch instead of alloc because
it's easier to use than bulksubmit.

```bash
$ flux batch -n1 ./larger/start.sh 
```

If you look in the output file, we are at least faking submitting the 100 jobs to include `burst[0-99]`. This is fake because:

- Those nodes don't actually exist
- We are asking for 6 nodes but we only really have 4 (and it seems to still "run")

```bash
$ cat flux-ƒLVJ2D4sq.out 
```
```console
$ cat flux-ƒLVJ2D4sq.out 
MATCH_FORMAT=rv1 NJOBS=10 NODES/JOB=6
{
  "match-format": "rv1"
}
     STATE NNODES   NCORES    NGPUS NODELIST
      free    104    10816        0 flux-sample[0-3],burst[0-99]
 allocated      0        0        0 
      down      0        0        0 
rv1             10    6     0.89    11.24       194313          495       425984
       JOBID USER     NAME       ST NTASKS NNODES     TIME INFO
     ƒPuMuVy flux     hostname   CD      6      6   0.211s burst[40-45]
     ƒPssvDf flux     hostname   CD      6      6   0.286s burst[46-51]
     ƒPssvDe flux     hostname   CD      6      6   0.286s burst[52-57]
     ƒPssvDd flux     hostname   CD      6      6   0.272s burst[58-63]
     ƒPrPvwK flux     hostname   CD      6      6   0.254s burst[64-69]
     ƒPrPvwJ flux     hostname   CD      6      6   0.237s burst[70-75]
     ƒPrPvwH flux     hostname   CD      6      6   0.220s burst[76-81]
     ƒPpuwey flux     hostname   CD      6      6   0.202s burst[82-87]
     ƒPpuwex flux     hostname   CD      6      6   0.185s burst[88-93]
     ƒPpuwew flux     hostname   CD      6      6   0.122s burst[94-99]
{
  "t_depend": 1687838671.51842,
  "t_run": 1687838671.9197195,
  "t_cleanup": 1687838672.1305885,
  "t_inactive": 1687838672.1725576,
  "duration": 0,
  "expiration": 4841438671,
  "name": "hostname",
  "cwd": "/tmp/workflow",
  "ntasks": 6,
  "ncores": 624,
  "nnodes": 6,
  "priority": 16,
  "ranks": "[44-49]",
  "nodelist": "burst[40-45]",
  "success": true,
  "result": "COMPLETED",
  "waitstatus": 0,
  "id": 15032385536,
  "t_submit": 1687838671.505264,
  "state": "INACTIVE",
  "username": "flux",
  "userid": 1000,
  "urgency": 16,
  "runtime": 0.21086907386779785,
  "status": "COMPLETED",
  "returncode": 0,
  "dependencies": [],
  "annotations": {},
  "exception": {
    "occurred": false
  }
}
```

For background about how this is working, see [this discussion](https://github.com/flux-framework/flux-sched/issues/1009#issuecomment-1610039068).

## Combined 

> Submit some actual (working/running) jobs and mock jobs.

```bash
$ flux batch -N 3 ./combined/start.sh 
```

Note that we are selecting 3/4 nodes, and then will get the hostlist dynamically
to know which we got! I want to have a combination of working and faux - and this is still a WIP!
You can find [discussion here](https://github.com/flux-framework/flux-core/issues/5295).

```console
MATCH_FORMAT=rv1 NJOBS=10 NODES/JOB=6
The Hostlist is...
flux-sample-[1-3]

{
  "match-format": "rv1"
}
     STATE QUEUE      NNODES   NCORES    NGPUS NODELIST
      free online          3        9        0 flux-sample-[1-3]
      free offline       100    10300        0 burst[0-99]
 allocated                 0        0        0 
      down                 0        0        0 
0 flux-sample-1: full
├─ 1 flux-sample-2: full
└─ 2 flux-sample-3: full
     STATE UP NNODES NODELIST
     avail  ✔      3 flux-sample-[1-3]
    avail*  ✗    100 burst[0-99]
ƒyWud5R
rv1             10    6     1.22     8.20         1758          563       454656
flux-sample-3
       JOBID QUEUE    USER     NAME       ST NTASKS NNODES     TIME INFO
     ƒyWud5R online   flux     hostname   CD      1      1   0.036s flux-sample-3
     ƒd4sXdb offline  flux     hostname   CD      6      6   0.121s burst[40-45]
     ƒd4sXda offline  flux     hostname   CD      6      6   0.172s burst[46-51]
     ƒd4sXdZ offline  flux     hostname   CD      6      6   0.172s burst[52-57]
     ƒd3PYMF offline  flux     hostname   CD      6      6   0.159s burst[58-63]
     ƒd3PYME offline  flux     hostname   CD      6      6   0.148s burst[64-69]
     ƒd3PYMD offline  flux     hostname   CD      6      6   0.137s burst[70-75]
     ƒd1uZ4u offline  flux     hostname   CD      6      6   0.125s burst[76-81]
     ƒd1uZ4t offline  flux     hostname   CD      6      6   0.113s burst[82-87]
     ƒd1uZ4s offline  flux     hostname   CD      6      6   0.102s burst[88-93]
     ƒczRZnX offline  flux     hostname   CD      6      6   0.080s burst[94-99]
{
  "t_depend": 1687976241.7190528,
  "t_run": 1687976241.7324638,
  "t_cleanup": 1687976241.7688088,
  "t_inactive": 1687976241.7703216,
  "duration": 0,
  "expiration": 4841576241,
  "name": "hostname",
  "cwd": "/tmp/workflow",
  "queue": "online",
  "ntasks": 1,
  "ncores": 3,
  "nnodes": 1,
  "priority": 16,
  "ranks": "2",
  "nodelist": "flux-sample-3",
  "success": true,
  "result": "COMPLETED",
  "waitstatus": 0,
  "id": 37094424576,
  "t_submit": 1687976241.707649,
  "state": "INACTIVE",
  "username": "flux",
  "userid": 1000,
  "urgency": 16,
  "runtime": 0.03634500503540039,
  "status": "COMPLETED",
  "returncode": 0,
  "dependencies": [],
  "annotations": {},
  "exception": {
    "occurred": false
  }
}
```

Note that if we provide all the sample workers in the broker spec, we need
to do `-N 4`. I'm not sure if there is a way to know some -n1 worker and then write
it to the underlying spec as the new parent.
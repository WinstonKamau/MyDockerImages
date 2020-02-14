A docker container that I can use to test on how readiness probes and liveness probes work on Kubernetes.

# Setup

Build and run with `docker-compose up --build`

## Test 1
To understand if the readiness probe is only pinged when starting a pod and not pinged during the lifetime of the pod.

- With the values for k8s deployment file set as below:
```
          initialDelaySeconds: 1
          periodSeconds: 3
          timeoutSeconds: 3
          successThreshold: 1
          failureThreshold: 1
```
- I got the following logs when I deployed the app.
```
10.28.32.1 - - [14/Feb/2020:22:07:35 +0000] "GET /readiness-health-check HTTP/1.1" 200 24 "-" "kube-probe/1.15+"
10.28.32.1 - - [14/Feb/2020:22:07:37 +0000] "GET /liveness-health-check HTTP/1.1" 200 22 "-" "kube-probe/1.15+"
10.28.32.1 - - [14/Feb/2020:22:07:38 +0000] "GET /readiness-health-check HTTP/1.1" 200 24 "-" "kube-probe/1.15+"
10.28.32.1 - - [14/Feb/2020:22:07:40 +0000] "GET /liveness-health-check HTTP/1.1" 200 22 "-" "kube-probe/1.15+"
10.28.32.1 - - [14/Feb/2020:22:07:41 +0000] "GET /readiness-health-check HTTP/1.1" 200 24 "-" "kube-probe/1.15+"
10.28.32.1 - - [14/Feb/2020:22:07:43 +0000] "GET /liveness-health-check HTTP/1.1" 200 22 "-" "kube-probe/1.15+"
10.28.32.1 - - [14/Feb/2020:22:07:44 +0000] "GET /readiness-health-check HTTP/1.1" 200 24 "-" "kube-probe/1.15+"
10.28.32.1 - - [14/Feb/2020:22:07:46 +0000] "GET /liveness-health-check HTTP/1.1" 200 22 "-" "kube-probe/1.15+"
10.28.32.1 - - [14/Feb/2020:22:07:47 +0000] "GET /readiness-health-check HTTP/1.1" 200 24 "-" "kube-probe/1.15+"
10.28.32.1 - - [14/Feb/2020:22:07:49 +0000] "GET /liveness-health-check HTTP/1.1" 200 22 "-" "kube-probe/1.15+"
10.28.32.1 - - [14/Feb/2020:22:07:50 +0000] "GET /readiness-health-check HTTP/1.1" 200 24 "-" "kube-probe/1.15+"
10.28.32.1 - - [14/Feb/2020:22:07:52 +0000] "GET /liveness-health-check HTTP/1.1" 200 22 "-" "kube-probe/1.15+"
10.28.32.1 - - [14/Feb/2020:22:07:53 +0000] "GET /readiness-health-check HTTP/1.1" 200 24 "-" "kube-probe/1.15+"
10.28.32.1 - - [14/Feb/2020:22:07:55 +0000] "GET /liveness-health-check HTTP/1.1" 200 22 "-" "kube-probe/1.15+"
10.28.32.1 - - [14/Feb/2020:22:07:56 +0000] "GET /readiness-health-check HTTP/1.1" 200 24 "-" "kube-probe/1.15+"
10.28.32.1 - - [14/Feb/2020:22:07:58 +0000] "GET /liveness-health-check HTTP/1.1" 200 22 "-" "kube-probe/1.15+"
10.28.32.1 - - [14/Feb/2020:22:07:59 +0000] "GET /readiness-health-check HTTP/1.1" 200 24 "-" "kube-probe/1.15+"
10.28.32.1 - - [14/Feb/2020:22:08:01 +0000] "GET /liveness-health-check HTTP/1.1" 200 22 "-" "kube-probe/1.15+"
10.28.32.1 - - [14/Feb/2020:22:08:02 +0000] "GET /readiness-health-check HTTP/1.1" 200 24 "-" "kube-probe/1.15+"
10.28.32.1 - - [14/Feb/2020:22:08:04 +0000] "GET /liveness-health-check HTTP/1.1" 200 22 "-" "kube-probe/1.15+"
10.28.32.1 - - [14/Feb/2020:22:08:05 +0000] "GET /readiness-health-check HTTP/1.1" 200 24 "-" "kube-probe/1.15+"
10.28.32.1 - - [14/Feb/2020:22:08:07 +0000] "GET /liveness-health-check HTTP/1.1" 200 22 "-" "kube-probe/1.15+"
10.28.32.1 - - [14/Feb/2020:22:08:08 +0000] "GET /readiness-health-check HTTP/1.1" 200 24 "-" "kube-probe/1.15+"
10.28.32.1 - - [14/Feb/2020:22:08:10 +0000] "GET /liveness-health-check HTTP/1.1" 200 22 "-" "kube-probe/1.15+"
10.28.32.1 - - [14/Feb/2020:22:08:11 +0000] "GET /readiness-health-check HTTP/1.1" 200 24 "-" "kube-probe/1.15+"
10.28.32.1 - - [14/Feb/2020:22:08:13 +0000] "GET /liveness-health-check HTTP/1.1" 200 22 "-" "kube-probe/1.15+"
10.28.32.1 - - [14/Feb/2020:22:08:14 +0000] "GET /readiness-health-check HTTP/1.1" 200 24 "-" "kube-probe/1.15+"
```

**Conclusion:** The readiness probe does continue checking if the app is able to serve requests and hence is still used by the Service object for loadbalancing.
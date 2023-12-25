# flake8: noqa
import os

phase = int(os.environ["TEST_PHASE"])
phase1 = (phase == 1)
phase2 = (phase == 2)

ktor.app.register_plugin("minikube", k8s_version="1.28.4",
                         start_fresh=phase1, keep_running=phase1, profile="issue-122480")
ktor.app.register_plugin("k8s")


def add_topologykeys_service(resources, r: "K8SResource"):
    if r.kind == "Service":
        spec = r.manifest["spec"]
        if ("clusterIP" not in r.manifest["spec"] or (
                "clusterIP" in r.manifest["spec"] and r.manifest["spec"]["clusterIP"] != "None")):
            spec["topologyKeys"] = ["kubernetes.io/hostname", "topology.kubernetes.io/zone",
                                    "topology.kubernetes.io/region", "*"]
            logger.warning("Added topology keys to %s", r.key)


ktor.k8s.add_transformer(add_topologykeys_service)



import logging
import http.client as http_client

http_client.HTTPConnection.debuglevel = 1
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

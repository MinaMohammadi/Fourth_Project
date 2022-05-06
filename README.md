# K8S-kubernetes

```
$ usdo iptables --flush (-F)

$ sudo vim /etc/sysctl.conf
or
$ sudo echo 1 > /proc/sys/net/ipv4/ip_forward
> net.ipv4.ip_forward = 1

$ sudo sysctl -p /etc/sysctl.conf
 net.ipv4.ip_forward = 1

```

```
sudo apt-mark hold kubelet kubeadm kubectl
docker info | grep -i cgroup
echo "Environment="KUBELET_CGROUP_ARGS=--cgroup-driver-cgroupfs"" >> /etc/systemd/system/kubelet.service.d/10-kubeadm.conf
systemctl restart kubelet
systemctl daemon-reload
```

```
sudo tee /etc/sysctl.d/kubernetes.conf<<EOF
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1
EOF

sudo sysctl --system
```
# general 
```
kubectl version --client
kubectl get nodes -o wide
kubectl cluster-info  
kubectl -n kube-system edit svc 
kubectl get pods --all-namespaces
kubectl get pods -n kube-system
```

```
The connection to the server localhost:8080 was refused - did you specify the right host or port?
$ cp /etc/kubernetes/admin.conf $HOME/
$ chown  $(id -u) $HOME/admin.conf
$ export KUBECONFIG=$HOME/admin.conf
```

# work with pods and nodes:
nodes are the servers and containers are built in pods.
```
kubectl get nodes
kubectl get pods
kubectl get pods --namespace=default
kubectl get namespaces
```
# create pods:
smallest unit of the kubernertes.
```
kubectl run nginx --image=nginx
docker ps | nginx
kubectl describe nginx
kubectl get pods -o wide
kubectl delete pod nginx
kubectl apply -f nginx-pod.yml
```
# create alias letter for kubectl :)
make it shorter and smaller.
```
alias k="kubectl"
```
# work with deployment
increase, decrease and modify pods easily. pods are managed by deployments.
```
kubectl create deployment deplo-nginx --image==nginx 
kubectl get deployment
kubectl describe deployment deyplo-nginx
kubectl describe pod deplo-nginx-56b84c4659-89vwg
kubectl scale deployment deplo-nginx --replicas=5
kubectl get deployment deplo-ngixn -o yaml
kubectl edit deployment deplo-nginx 
```
# create service for deployment
create service for a deployment. instead of using IP add per pod, we can use a virtual ip address for entire a deploy which is created by k8s. this ip add is reachable only inside of the cluster and we can talk with all pods inside that deployment with this single IP. It is hidden from outside world.
```
kubectl expose deployment deplo-nginx --port=8080 --target-port=80
kubectl get services -> svc
kubectl describe svc deplo-nginx
kubectl delete deployment deplo-nginx
kubectl delete service deplo-nginx
```
# create nodeport service
from this way deployment is avaiable outside of the cluster (specific random port)
```
kubectl expose deployment deplo1-nginx --type=NodePort --port=80
kubectl expose deployment deplo1-nginx --type=LoadBalancer --port=80
```
# debug kubernetes
```
kubectl logs pod-name
kubectl describe pod deplo-nginx
kubectl exec -it pod-name -- bash -n namespace
kubectl logs <pod-name> -n <namespace> --previous
```
# namespace-port forwarding
```
kubectl get namespaces
kubectl create ns kafka
kubectl get pods -n kafka
kubectl config set-context --current --namespace=kafka
kubectl port-forward redis-master-765d459796-258hz 6379:6379 
```
# configmap
```
kubectl get configmap
kubectl get cm
```
# kafka-topics
```
kafka-topics.sh --create --zookeeper 10.244.2.28:2181 --replication-factor 1 --partitions 1 --topic output
bin/kafka-topics.sh --list --zookeeper 10.244.2.28:2181
```
# join nodes to cluster
Kubeadm HA | Adding additional master nodes to the cluster
```
sudo kubeadm init phase upload-certs --upload-certs
sudo kubeadm token create --certificate-key 84e102e981f36b68527f7e6b7af628666531aacdbb38c1234e7b85e817b7a6e4 --print-join-command
```
# setup kubernetes dashboard
```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.4.0/aio/deploy/recommended.yaml
kubectl get nameapasce
kubectl get pods -n kubernetes-dashboard

# nodeport or port-forwarding ?
portforwarding:
- find actual port of the service
> kubectl -n kubernetes-dashboard  describe svc kubernetes-dashboard
> kubectl -n kubernetes-dashboard port-forward pod-name 8000:8443
nodeport:
> kubectl -n kubernetes-dashboard edit svc kubernetes-dashboard 
- type: NodePort and nodePort: 32323

Token:
kubectl get sa -n kubernetes-dashboard
kubectl describe sa kubernetes-dashboard -n kubernetes-dashboard
kubectl describe secret kubernetes-dashboard-token-ktghf -n kubernetes-dashboard
```


kubectl create deployment nginx --image=nginx
kubectl create service nodeport nginx --tcp=80:80
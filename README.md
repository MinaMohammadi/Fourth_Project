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

```
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
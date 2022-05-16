# Kustomization

kustomize lets you customize raw, template-free YAML files for multiple purposes, leaving the original YAML untouched and usable as is.
kustomize targets kubernetes; it understands and can patch kubernetes style API objects. It's like make, in that what it does is declared in a file, and it's like sed, in that it emits edited text
```
wget https://github.com/kubernetes-sigs/kustomize/releases/download/kustomize%2Fv4.5.3/kustomize_v4.5.3_linux_amd64.tar.gz
```
then extract it:

```
tar zxf kustomize_v4.5.3_linux_amd64.tar.gz
```
move binary files to bin:

```
sudo mv kustomize /usr/local/bin
```
Generate customized YAML with:

```
kustomize build ~/someApp
```
The YAML can be directly applied to a cluster:

```
kustomize build ~/someApp | kubectl apply -f -
```
For more information:
* [Kustomization](https://github.com/kubernetes-sigs/kustomize)

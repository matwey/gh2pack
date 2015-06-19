#gh2pack
##Usage example
```
osc mkpac go-raft-boltdb
pushd go-raft-boltdb
gh2pack generate hashicorp raft-boltdb --template=_service
gh2pack generate hashicorp raft-boltdb --filename=go-raft-boltdb.spec
osc vc -m "Initial version"
osc add _service go-raft-boltdb.spec go-raft-boltdb.changes
osc commit
osc service dr
osc add *.tar.bz2
osc add _servicedata
osc service localrun format_spec_file
osc commit
```

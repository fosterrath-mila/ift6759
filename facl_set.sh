#!/usr/bin/env bash -x

pushd /project/cq-training-1/

# Normalize parent directories
setfacl -m default:group:cq-training-1:r-x\
        -m group:cq-training-1:r-x\
        .
setfacl -m default:group:cq-training-1:r-x\
        -m group:cq-training-1:r-x\
        project?
setfacl -m default:group:cq-training-1:r-x\
        -m group:cq-training-1:r-x\
        project?/{submissions,teams}
setfacl -x group:cq-training-1\
        -x default:group:cq-training-1\
        project?/{submissions,teams}/team??
setfacl -m group:cq-training-1:r-x\
        -m default:group:cq-training-1:r-x\
        project?/data

# User group definitions
setfacl -d -m user:guest111:rwx\
        -d -m user:guest112:rwx\
        -d -m user:guest113:rwx\
        -d -m user:guest114:rwx\
        project?/{submissions,teams}/team01
setfacl -d -m user:guest115:---\
        -d -m user:guest116:rwx\
        -d -m user:guest117:---\
        -d -m user:guest118:rwx\
        -d -m user:guest162:rwx\
        -d -m user:guest154:rwx\
        project?/{submissions,teams}/team02
setfacl -d -m user:guest119:rwx\
        -d -m user:guest120:rwx\
        -d -m user:guest121:rwx\
        -d -m user:guest122:rwx\
        project?/{submissions,teams}/team03
setfacl -d -m user:guest123:rwx\
        -d -m user:guest124:rwx\
        -d -m user:guest125:rwx\
        -d -m user:guest126:rwx\
        project?/{submissions,teams}/team04
setfacl -d -m user:guest127:rwx\
        -d -m user:guest128:---\
        -d -m user:guest129:rwx\
        -d -m user:guest130:rwx\
        -d -m user:guest170:rwx\
        project?/{submissions,teams}/team05
setfacl -d -m user:guest131:rwx\
        -d -m user:guest132:rwx\
        -d -m user:guest133:rwx\
        -d -m user:guest134:rwx\
        project?/{submissions,teams}/team06
setfacl -d -m user:guest135:rwx\
        -d -m user:guest136:rwx\
        -d -m user:guest137:rwx\
        -d -m user:guest138:rwx\
        project?/{submissions,teams}/team07
setfacl -d -m user:guest139:rwx\
        -d -m user:guest140:rwx\
        -d -m user:guest141:rwx\
        -d -m user:guest142:rwx\
        project?/{submissions,teams}/team08
setfacl -d -m user:guest143:rwx\
        -d -m user:guest144:rwx\
        -d -m user:guest145:rwx\
        -d -m user:guest146:rwx\
        project?/{submissions,teams}/team09
setfacl -d -m user:guest147:rwx\
        -d -m user:guest148:rwx\
        -d -m user:guest149:rwx\
        -d -m user:guest150:rwx\
        project?/{submissions,teams}/team10
setfacl -d -m user:guest151:rwx\
        -d -m user:guest152:rwx\
        -d -m user:guest153:rwx\
        -d -m user:guest154:---\
        -d -m user:guest169:rwx\
        project?/{submissions,teams}/team11
setfacl -d -m user:guest155:rwx\
        -d -m user:guest156:rwx\
        -d -m user:guest157:rwx\
        -d -m user:guest158:rwx\
        project?/{submissions,teams}/team12
setfacl -d -m user:guest159:rwx\
        -d -m user:guest160:rwx\
        -d -m user:guest161:rwx\
        -d -m user:guest162:---\
        -d -m user:guest168:rwx\
        -d -m user:guest170:---\
        project?/{submissions,teams}/team13
setfacl -d -m user:guest163:rwx\
        -d -m user:guest164:rwx\
        -d -m user:guest165:rwx\
        -d -m user:guest166:rwx\
        -d -m user:guest167:---\
        project?/{submissions,teams}/team14

popd

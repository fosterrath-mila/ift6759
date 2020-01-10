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
setfacl -m user:guest111:rwx\
        -m user:guest112:rwx\
        -m user:guest113:rwx\
        -m user:guest114:rwx\
        project?/{submissions,teams}/team01
setfacl -m user:guest115:rwx\
        -m user:guest116:rwx\
        -m user:guest117:rwx\
        -m user:guest118:rwx\
        project?/{submissions,teams}/team02
setfacl -m user:guest119:rwx\
        -m user:guest120:rwx\
        -m user:guest121:rwx\
        -m user:guest122:rwx\
        project?/{submissions,teams}/team03
setfacl -m user:guest123:rwx\
        -m user:guest124:rwx\
        -m user:guest125:rwx\
        -m user:guest126:rwx\
        project?/{submissions,teams}/team04
setfacl -m user:guest127:rwx\
        -m user:guest128:rwx\
        -m user:guest129:rwx\
        -m user:guest130:rwx\
        project?/{submissions,teams}/team05
setfacl -m user:guest131:rwx\
        -m user:guest132:rwx\
        -m user:guest133:rwx\
        -m user:guest134:rwx\
        project?/{submissions,teams}/team06
setfacl -m user:guest135:rwx\
        -m user:guest136:rwx\
        -m user:guest137:rwx\
        -m user:guest138:rwx\
        project?/{submissions,teams}/team07
setfacl -m user:guest139:rwx\
        -m user:guest140:rwx\
        -m user:guest141:rwx\
        -m user:guest142:rwx\
        project?/{submissions,teams}/team08
setfacl -m user:guest143:rwx\
        -m user:guest144:rwx\
        -m user:guest145:rwx\
        -m user:guest146:rwx\
        project?/{submissions,teams}/team09
setfacl -m user:guest147:rwx\
        -m user:guest148:rwx\
        -m user:guest149:rwx\
        -m user:guest150:rwx\
        project?/{submissions,teams}/team10
setfacl -m user:guest151:rwx\
        -m user:guest152:rwx\
        -m user:guest153:rwx\
        -m user:guest154:rwx\
        project?/{submissions,teams}/team11
setfacl -m user:guest155:rwx\
        -m user:guest156:rwx\
        -m user:guest157:rwx\
        -m user:guest158:rwx\
        project?/{submissions,teams}/team12
setfacl -m user:guest159:rwx\
        -m user:guest160:rwx\
        -m user:guest161:rwx\
        -m user:guest162:rwx\
        -m user:guest168:rwx\
        project?/{submissions,teams}/team13
setfacl -m user:guest163:rwx\
        -m user:guest164:rwx\
        -m user:guest165:rwx\
        -m user:guest166:rwx\
        -m user:guest167:rwx\
        project?/{submissions,teams}/team14

popd

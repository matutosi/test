import streamlit as st

import os
import sys
import glob
import pathlib
import tempfile

def tree(path, layer=0, is_last=False, indent_current='　'):
    if not pathlib.Path(path).is_absolute():
        path = str(pathlib.Path(path).resolve())
    # カレントディレクトリの表示
    current = path.split('/')[::-1][0]
    if layer == 0:
        st.write('<'+current+'>')
    else:
        branch = '└' if is_last else '├'
        st.write('{indent}{branch}<{dirname}>'.format(indent=indent_current, branch=branch, dirname=current))
    # 下の階層のパスを取得
    paths = [p for p in glob.glob(path+'/*') if os.path.isdir(p) or os.path.isfile(p)]
    def is_last_path(i):
        return i == len(paths)-1
    # 再帰的に表示
    for i, p in enumerate(paths):
        indent_lower = indent_current
        if layer != 0:
            indent_lower += '　　' if is_last else '│　'
        if os.path.isfile(p):
            branch = '└' if is_last_path(i) else '├'
            st.write('{indent}{branch}{filename}'.format(indent=indent_lower, branch=branch, filename=p.split('/')[::-1][0]))
        if os.path.isdir(p):
            tree(p, layer=layer+1, is_last=is_last_path(i), indent_current=indent_lower)


st.write("\nsys.path-------------------")
for p in sys.path:
    st.write(p)

st.write(f'\nWD: {os.getcwd()}')
st.write("\nlistdir-------------------")
for l in os.listdir():
    st.write(l)

st.write("\ntree-------------------")
tree(".")

tmp_dir = os.path.join(tempfile.TemporaryDirectory().name, "")
os.makedirs(tmp_dir, exist_ok=True)

st.write("\nTMP_DIR-------------------")
st.write(f'tmp_dir: {tmp_dir}')


st.write("\nchdir-------------------")
os.chdir(tmp_dir)
st.write(f'WD: {os.getcwd()}')

st.write("\nlistdir-------------------")
for l in os.listdir():
    st.write(l)

st.write("\ntree . -------------------")
tree(".")

st.write("\ntree /mount/src/comptea/-------------------")
tree("/mount/src/comptea/")

st.write("finished")

import subprocess

for i in range(1021):  # 1021 is the number of problems
    bash_script = f'python try/agent_ds.py \
     try/HLE/problem{str(i+1).zfill(4)}.txt \
     --log try/log/agent_output{str(i+1).zfill(4)}.log'  # this fit my GPU style
    subprocess.run(
        ["bash", "-c", bash_script],  # use lists to import commands and parameters
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8"
    )

#!/usr/bin/python3

import subprocess
import argparse
import random


def classifyImagePython(network="googlenet", url="https://a-z-animals.com/media/animals/images/original/chameleon2.jpg"):
    processWord = ''
    if network != "googlenet":
        network = "resnet18.onnx"
    if "http" in url:
        process = subprocess.run(f"wget {url} -O perSessionImageName.jpg", stdout=subprocess.PIPE, shell=True)
        filename = "perSessionImageName.jpg"
    else:
        filename = url

    process = subprocess.run(f"sh run.sh --network={network} {filename}", stdout=subprocess.PIPE, shell=True)
    process = process.stdout.decode('utf-8')
    processIndex = process.find("recognized")

    while process[processIndex] != "ㅒ":
        processWord += process[processIndex]
        processIndex += 1
    

    return processWord
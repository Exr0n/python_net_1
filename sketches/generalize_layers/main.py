# Created Mon 05 Aug 2019 @ 22:54 CST
import numpy as np
import random

config = {
    "structure": {
        "input": 3,
        "hidden": [4],
        "output": 1
    },
    "data": {
        "length": 4
    },
    "test": {
        "cycles": 60000,
        "print_error": 10000,
        "random_seed": "random"
    }
}


input = np.array([[0, 0, 1],
                  [0, 1, 1],
                  [1, 0, 1],
                  [1, 1, 1]])

expect = np.array([[0],
                   [1],
                   [1],
                   [0]])

(config.data.length, config.structure.input) = input.size
(_, config.structure.output) = expect.size


def nonlin(x, deriv=False):
    if (deriv is True):
        return x*(1-x)
    return 1/(1+np.exp(-x))


if (config.random_seed == "random"):
    r = int(random.random()*10**9)
    print(f"Random seed: {r}")
    config.random_seed = r
np.random.seed(config.random_seed)

# randomly initialize our weights with mean 0
synapses = []
t_prev = config.structure.input
for size in (config.structure.hidden + [config.structure.output]):
    synapses.append(2*np.random.random((t_prev, size))-1)
    t_prev = size

for j in range(config.test.cycles):

    # Feed forward through layers 0, 1, and 2
    layers = [input]
    for (idx, syn) in synapses:
        layers[idx+1] = nonlin(np.dot(layers[idx], syn))

    l_error = [0] * len(layers)-1
    l_delta = l_error
    l_delta.push(expect-layers[-1])

    for i, c in enumerate(reversed(layers)):
        l_error[-i-1] = l_delta[-i-1].dot(layers[-i-1].T)
        l_delta[-i-2] = l_error[-i-1] * nonlin(layers[-i-1], True)

    # how much did we miss the target value?
    l2_error = y - l2

    if (j % config.print_error) == 0:
        print("Error:" + str(np.mean(np.abs(l2_error))))

    # in what direction is the target value?
    # were we really sure? if so, don't change too much.
    l2_delta = l2_error*nonlin(l2, deriv=True)

    # how much did each l1 value contribute to the l2 error (by the weights)?
    l1_error = l2_delta.dot(syn1.T)  # todo

    # in what direction is the target l1?
    # were we really sure? if so, don't change too much.
    l1_delta = l1_error * nonlin(l1, deriv=True)

    syn1 += l1.T.dot(l2_delta)  # todo
    syn0 += l0.T.dot(l1_delta)

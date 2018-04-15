#!/usr/bin/python

import sys
import random
import numpy


def main(args):
    n_repetitions = int(args[1])
    total_time = int(args[2])
    n_cashiers = int(args[3])
    service_time_param = int(args[4])
    distribution_param = float(args[5])
    cashiers = [0] * n_cashiers
    accepted_requests = 0
    rejected_requests = 0
    next_client = 0
    queue = []
    max_wait_list = []
    accepted_list = []
    rejected_list = []
    next_client_list = []
    time_cashiers_list = []

    for repetition in range(0, n_repetitions):
        accepted_requests = 0
        rejected_requests = 0
        next_client = 0
        max_wait = 0
        # import ipdb;ipdb.set_trace()
        for current_time in range(0, total_time):
            if next_client == current_time:
                while next_client == current_time:
                    aux = poisson(distribution_param)
                    next_client_list.append(aux)
                    next_client = current_time + aux
                    if (current_time + next_client) > total_time:
                        break
                    if accept_queue(len(queue), n_cashiers):
                        if 0 in cashiers:
                            index = cashiers.index(0)
                            aux = poisson(service_time_param)
                            time_cashiers_list.append(aux)
                            cashiers[index] = aux
                            queue.insert(0, 0)
                        accepted_requests += 1
                    else:
                        rejected_requests += 1

            for i in range(0, len(cashiers)):
                cashiers[i] = max(cashiers[i] - 1, 0)
                if cashiers[i] == 0 and len(queue) > 0:
                    aux = poisson(service_time_param)
                    time_cashiers_list.append(aux)
                    cashiers[index] = aux
                    t = queue.pop()
                    max_wait = max(max_wait, t)

            queue = map(lambda x: x + 1, queue)
        max_wait_list.append(max_wait)
        accepted_list.append(accepted_requests)
        rejected_list.append(rejected_requests)

        if repetition % 100 == 0 and repetition != 0:
            print_results(
                accepted_list, rejected_list, max_wait_list,
                time_cashiers_list, next_client_list
            )


def poisson(param):
    return numpy.random.poisson(param)


def print_results(
        accepts, rejects,
        waits, time_cashiers_list,
        next_client_list
                  ):

    print 'Accepted: {}; Rejected: {}; Medium:{}, '\
          ' Wait:{}, Cashier:{}, Client:{}'.format(
            (float(sum(accepts))/float(len(accepts))),
            (float(sum(rejects))/float(len(rejects))),
            (float(sum(rejects)) / float(sum(accepts) + sum(rejects))),
            (float(sum(waits))/float(len(waits))),
            (float(sum(time_cashiers_list))/float(len(time_cashiers_list))),
            (float(sum(next_client_list))/float(len(next_client_list))),
                                                    )


def accept_queue(queue, n_cashiers):
    prob = float(queue) / (float(queue) + float(n_cashiers))
    rand = random.random()
    return prob < rand


main(sys.argv)

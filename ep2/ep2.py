#!/usr/bin/python

import sys
import numpy


def main(args):
    n_repetitions = int(args[1])
    total_time = int(args[2])
    lines = [0] * int(args[3])
    distribution_param = int(args[4])
    service_time = int(args[5])
    accepted_list = []
    rejected_list = []

    for repetition in range(0, n_repetitions):
        accepted_requests = 0
        rejected_requests = 0
        next_request = 0
        for current_time in range(0, total_time):
            if next_request == current_time:
                while next_request == current_time:
                    next_request = (
                        current_time + poisson(distribution_param)
                    )
                    if (current_time + service_time) > total_time:
                        break
                    if 0 in lines:
                        index = lines.index(0)
                        lines[index] = service_time*6
                        accepted_requests += 1
                    else:
                        rejected_requests += 1
            lines = map(lambda x: max(x-1, 0), lines)
        accepted_list.append(accepted_requests)
        rejected_list.append(rejected_requests)

        if repetition % 100 == 0 and repetition != 0:
            print_results(accepted_list, rejected_list)


def poisson(media):
    return numpy.random.poisson(media)


def print_results(accepts, rejects):
    print 'Accepted: {}; Rejected: {}; Medium:{}'.format(
        (float(sum(accepts))/float(len(accepts))),
        (float(sum(rejects))/float(len(rejects))),
        (float(sum(rejects)) / float(sum(accepts) + sum(rejects)))
    )

main(sys.argv)

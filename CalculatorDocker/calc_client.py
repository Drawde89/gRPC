# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging

import grpc
import calc_pb2
import calc_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calc_pb2_grpc.CalculatorStub(channel)
        
        not_quit = True

        while not_quit:
            print('CALCULATOR')
            print('The valid operators are "+", "-", "*", "/" or enter "q" to quit\n')            
            operator = str(input('Enter Your Operator Or Quit: '))
            if operator == 'q':
                not_quit = False
                print('Quitting.....')
            else:
                fTerm = str(input('Enter Your First Term: '))
                sTerm = str(input('Enter Your Second Term: '))
                print()
                try:
                    #returns the servers message after the items that satisfy the proto buffer are passed through
                    response = stub.Calc(calc_pb2.CalcRequest(firstTerm = fTerm, secondTerm = sTerm, oper = operator))     
                    print(f'{response.message}')
                except:
                    print('\n**Cannot Reach Server. Did you Turn the server on?**')
                    not_quit = False   

if __name__ == '__main__':
    logging.basicConfig()
    run()

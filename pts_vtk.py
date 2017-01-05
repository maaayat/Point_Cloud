#from numpy import genfromtxt
#my_data = genfromtxt('teepeetest', delimiter=' ')
import csv
import numpy as np
import sys, time
import pp

with open('teepeetest','r') as dest_f:
    data_iter = csv.reader(dest_f, 
                           delimiter = " ", 
                           quotechar = '"')
    data = [data for data in data_iter]
data_array = np.asarray(data, dtype = np.dtype(float))  
#print str(data_array)[1:-1]
def pts_vtk(data_array):
	from evtk.hl import pointsToVTK
	pointsToVTK("./points", data_array[:,0], data_array[:,1], data_array[:,2], data = {"C" : data_array[:,3]})
return True


"""def isprime(n):
    #Returns True if n is prime and False otherwise
    if not isinstance(n, int):
        raise TypeError("argument passed to is_prime is not of 'int' type")
    if n < 2:
        return False
    if n == 2:
        return True
    max = int(math.ceil(math.sqrt(n)))
    i = 2
    while i <= max:
        if n % i == 0:
            return False
        i += 1
    return True"""

"""def sum_primes(n):
    #Calculates sum of all primes below given integer n
    return sum([x for x in xrange(2,n) if isprime(x)])"""

print """Usage: python pts_vtk.py [ncpus]
    [ncpus] - the number of workers to run in parallel, 
    if omitted it will be set to the number of processors in the system
"""

# tuple of all parallel python servers to connect with
ppservers = ()
#ppservers = ("10.0.0.1",)

if len(sys.argv) > 1:
    ncpus = int(sys.argv[1])
    # Creates jobserver with ncpus workers
    job_server = pp.Server(ncpus, ppservers=ppservers)
else:
    # Creates jobserver with automatically detected number of workers
    job_server = pp.Server(ppservers=ppservers)

print "Starting pp with", job_server.get_ncpus(), "workers"
start_time = time.time()

# Submit a job of calulating sum_primes(100) for execution. 
# sum_primes - the function
# (100,) - tuple with arguments for sum_primes
# (isprime,) - tuple with functions on which function sum_primes depends
# ("math",) - tuple with module names which must be imported before sum_primes execution
# Execution starts as soon as one of the workers will become available
job1 = job_server.submit(pts_vtk, (), (), ("csv","numpy",))

# Retrieves the result calculated by job1
# The value of job1() is the same as sum_primes(100)
# If the job has not been finished yet, execution will wait here until result is available
result = job1()

print "done!", result

print "Time elapsed: ", time.time() - start_time, "s"

"""# The following submits 8 jobs and then retrieves the results
inputs = (100000, 100100, 100200, 100300, 100400, 100500, 100600, 100700)
jobs = [(input, job_server.submit(sum_primes,(input,), (isprime,), ("math",))) for input in inputs]
for input, job in jobs:
    print "Sum of primes below", input, "is", job()"""


job_server.print_stats()

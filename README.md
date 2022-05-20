# Load Test Simulation with Fast API, Gunicorn, and Uvicorn Workers

## Prequisites
This project requires yarb, poetry with python 3.10, and docker.

## Load testing
Run `yarn docker:build` to to build the test app.

Run `yarn docker:run` to run the app (by default it's exposing port 80).

Run `yarn exec:loadtest` to run the loadtest.


## Results 

### Results using a single Gunicorn/Uvicorn worker.
Docker container ran with:
- 2GB memory (inconsequential, we're testing CPU load)
- "1" CPU
#### Individual Sync Load Test
Running 1000 total requests to `/sync-loadtest` in batches of 100 concurrent requests:

```
Server Software:        uvicorn
Server Hostname:        localhost
Server Port:            80

Document Path:          /sync-loadtest
Document Length:        38 bytes

Concurrency Level:      100
Time taken for tests:   26.374 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      163000 bytes
HTML transferred:       38000 bytes
Requests per second:    37.92 [#/sec] (mean)
Time per request:       2637.392 [ms] (mean)
Time per request:       26.374 [ms] (mean, across all concurrent requests)
Transfer rate:          6.04 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    1   1.9      0      11
Processing:  1005 2445 4921.4   1034   25346
Waiting:     1005 2444 4921.6   1032   25346
Total:       1005 2446 4921.9   1034   25352

Percentage of the requests served within a certain time (ms)
  50%   1034
  66%   1067
  75%   1835
  80%   1934
  90%   2090
  95%  12032
  98%  25266
  99%  25303
 100%  25352 (longest request)
✨  Done in 26.45s.

```

#### Individual Async Load Test

Running 10000 total requests to `async-loadtest`, in batches of 100 concurrent requests: 
```
Benchmarking localhost (be patient)
Completed 1000 requests
Completed 2000 requests
Completed 3000 requests
Completed 4000 requests
Completed 5000 requests
Completed 6000 requests
Completed 7000 requests
Completed 8000 requests
Completed 9000 requests
Completed 10000 requests
Finished 10000 requests


Server Software:        uvicorn
Server Hostname:        localhost
Server Port:            80

Document Path:          /async-loadtest
Document Length:        38 bytes

Concurrency Level:      100
Time taken for tests:   19.651 seconds
Complete requests:      10000
Failed requests:        0
Total transferred:      1630000 bytes
HTML transferred:       380000 bytes
Requests per second:    508.89 [#/sec] (mean)
Time per request:       196.507 [ms] (mean)
Time per request:       1.965 [ms] (mean, across all concurrent requests)
Transfer rate:          81.00 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    1   3.2      1     117
Processing:    12  194  72.6    173     585
Waiting:       12  175  67.5    155     511
Total:         22  195  72.9    174     586

Percentage of the requests served within a certain time (ms)
  50%    174
  66%    200
  75%    220
  80%    233
  90%    287
  95%    345
  98%    423
  99%    478
 100%    586 (longest request)
✨  Done in 19.73s.
```

The async load test pegged the CPU usage at over 100% (ideal, perfectly utilized async code), while the sync load test had single digit % CPU usage.

#### Running both the Sync and Async Load Tests simultaneously

- 10000 total requests to `async-loadtest`, in batches of 100 concurrent requests
- Running 1000 total requests to `/sync-loadtest` in batches of 100 concurrent requests:

Async load test results:
```
Server Software:        uvicorn
Server Hostname:        localhost
Server Port:            80

Document Path:          /async-loadtest
Document Length:        38 bytes

Concurrency Level:      100
Time taken for tests:   36.730 seconds
Complete requests:      10000
Failed requests:        0
Total transferred:      1630000 bytes
HTML transferred:       380000 bytes
Requests per second:    272.26 [#/sec] (mean)
Time per request:       367.298 [ms] (mean)
Time per request:       3.673 [ms] (mean, across all concurrent requests)
Transfer rate:          43.34 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    1   2.3      0     157
Processing:     5  365 1535.7     96   19174
Waiting:        5  354 1534.8     87   19163
Total:          5  365 1536.2     97   19174

Percentage of the requests served within a certain time (ms)
  50%     97
  66%    159
  75%    220
  80%    255
  90%    455
  95%   1111
  98%   1399
  99%   8085
 100%  19174 (longest request)
✨  Done in 36.81s.
```

Sync load test results:
```
Server Software:        uvicorn
Server Hostname:        localhost
Server Port:            80

Document Path:          /sync-loadtest
Document Length:        38 bytes

Concurrency Level:      100
Time taken for tests:   33.735 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      163000 bytes
HTML transferred:       38000 bytes
Requests per second:    29.64 [#/sec] (mean)
Time per request:       3373.488 [ms] (mean)
Time per request:       33.735 [ms] (mean, across all concurrent requests)
Transfer rate:          4.72 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    1   1.3      0       7
Processing:  1010 3005 5685.2   1152   32124
Waiting:     1008 2995 5682.6   1144   32096
Total:       1010 3006 5685.9   1152   32130

Percentage of the requests served within a certain time (ms)
  50%   1152
  66%   1294
  75%   1632
  80%   2073
  90%   4737
  95%  13888
  98%  31186
  99%  32088
 100%  32130 (longest request)
✨  Done in 33.86s.
```
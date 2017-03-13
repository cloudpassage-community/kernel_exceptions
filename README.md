# Halo Kernel Exceptions Management

Version: *1.0*
<br />
Author: *CloudPassage Integrations*

## Description

This script finds duplicate `Kernel` packages in a server and creates SVA exceptions for the non-running vulnerable kernel packages. 

## Requirements and Dependencies

* Python 2.7.10+
* Cloudpassage module ```pip install cloudpassage```

Place the following values inside of configs/portal.yml. The key_id and secret_key can be found from the Halo portal under Site Admin -> Api keys.

```
    key_id: 
    secret_key:
```

## Usage

```
usage: kernel_exceptions.py [-h] --expires_in EXPIRES_IN [--report]
                            [--execute]

Kernel Exception Management

optional arguments:
  -h, --help            show this help message and exit
  --expires_in EXPIRES_IN
                        Specify length of days to expire
  --report              Outputs (stdout) a list of servers with more than one
                        kernel package
  --execute             Adds exceptions for non-running extra kernels
```

## Modes

### Report mode
```
    python kernel_exceptions.py --expires_in=1 --report
```

### Execute mode (add exceptions for non-running kernel packages)
```
    python kernel_exceptions.py --expires_in=1 --execute
```

## License

Copyright (c) 2017, CloudPassage, Inc.
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the CloudPassage, Inc. nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL CLOUDPASSAGE, INC. BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED ANDON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

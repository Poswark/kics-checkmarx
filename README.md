# kics-checkmarx
Scanning  Infrastructure as Code - Secure


 curl -s -X GET http://localhost:5050  | jq
{
  "Hello": "World"
}

Share directory volume with container.

``` bash

docker run -t -v "$(pwd)/kics-checkmarx:/path" checkmarx/kics:latest scan -p /path



   MLLLLLM             MLLLLLLLLL   LLLLLLL             KLLLLLLLLLLLLLLLL       LLLLLLLLLLLLLLLLLLLLLLL
   MMMMMMM           MMMMMMMMMML    MMMMMMMK       LMMMMMMMMMMMMMMMMMMMML   KLMMMMMMMMMMMMMMMMMMMMMMMMM
   MMMMMMM         MMMMMMMMML       MMMMMMMK     LMMMMMMMMMMMMMMMMMMMMMML  LMMMMMMMMMMMMMMMMMMMMMMMMMMM
   MMMMMMM      MMMMMMMMMML         MMMMMMMK   LMMMMMMMMMMMMMMMMMMMMMMMML LMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   MMMMMMM    LMMMMMMMMML           MMMMMMMK  LMMMMMMMMMLLMLLLLLLLLLLLLLL LMMMMMMMLLLLLLLLLLLLLLLLLLLLM
   MMMMMMM  MMMMMMMMMLM             MMMMMMMK LMMMMMMMM                    LMMMMMML
   MMMMMMMLMMMMMMMML                MMMMMMMK MMMMMMML                     LMMMMMMMMLLLLLLLLLLLLLMLL
   MMMMMMMMMMMMMMMM                 MMMMMMMK MMMMMML                       LMMMMMMMMMMMMMMMMMMMMMMMMML
   MMMMMMMMMMMMMMMMMM               MMMMMMMK MMMMMMM                         LMMMMMMMMMMMMMMMMMMMMMMMML
   MMMMMMM KLMMMMMMMMML             MMMMMMMK LMMMMMMM                                          MMMMMMMML
   MMMMMMM    LMMMMMMMMMM           MMMMMMMK LMMMMMMMMLL                                        MMMMMMML
   MMMMMMM      LMMMMMMMMMLL        MMMMMMMK  LMMMMMMMMMMMMMMMMMMMMMMMMML LLLLLLLLLLLLLLLLLLLLMMMMMMMMMM
   MMMMMMM        MMMMMMMMMMML      MMMMMMMK   MMMMMMMMMMMMMMMMMMMMMMMMML LMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   MMMMMMM          LLMMMMMMMMML    MMMMMMMK     LLMMMMMMMMMMMMMMMMMMMMML LMMMMMMMMMMMMMMMMMMMMMMMMMML
   MMMMMMM             MMMMMMMMMML  MMMMMMMK         KLMMMMMMMMMMMMMMMMML LMMMMMMMMMMMMMMMMMMMMMMMLK




Scanning with Keeping Infrastructure as Code Secure v2.1.3


Preparing Scan Assets: Done
Executing queries: [---------------------------------------------------] 100.00%



Multiple RUN, ADD, COPY, Instructions Listed, Severity: LOW, Results: 1
Description: Multiple commands (RUN, COPY, ADD) should be grouped in order to reduce the number of layers.
Platform: Dockerfile
CWE: 710
Learn more about this vulnerability: https://docs.kics.io/latest/queries/dockerfile-queries/0008c003-79aa-42d8-95b8-1c2fe37dbfe6

	[1]: ../../path/Dockerfile:6

		005: COPY ./requirements.txt /code/requirements.txt
		006: RUN apk update --no-cache
		007: RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


Results Summary:
CRITICAL: 0
HIGH: 1
MEDIUM: 5
LOW: 3
INFO: 0
TOTAL: 9

```

docker run -t -v "$(pwd)/kics-checkmarx:/path" checkmarx/kics:latest scan -p /path -o "$(pwd)/kics-result" --report-formats "json" --output-name kics-result
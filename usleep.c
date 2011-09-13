#define _XOPEN_SOURCE 500
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "ydata.h"
#include "yapi.h"
#include "pstdlib.h"

void Y_usleep(int nArgs)
{
  long milliseconds = YGetInteger(sp-nArgs+1);
  useconds_t us;
  us = (useconds_t)(milliseconds*1000l);
  usleep(us);
}

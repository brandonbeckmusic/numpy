#ifndef NUMPY_CORE_INCLUDE_NUMPY_NPY_OS_H_
#define NUMPY_CORE_INCLUDE_NUMPY_NPY_OS_H_

#if defined(linux) || defined(__linux) || defined(__linux__)
    #define NPY_OS_LINUX
#elif defined(__FreeBSD__) || defined(__NetBSD__) || \
            defined(__OpenBSD__) || defined(__DragonFly__)
    #define NPY_OS_BSD
    #ifdef __FreeBSD__
        #define NPY_OS_FREEBSD
    #elif defined(__NetBSD__)
        #define NPY_OS_NETBSD
    #elif defined(__OpenBSD__)
        #define NPY_OS_OPENBSD
    #elif defined(__DragonFly__)
        #define NPY_OS_DRAGONFLY
    #endif
#elif defined(sun) || defined(__sun)
    #define NPY_OS_SOLARIS
#elif defined(__CYGWIN__)
    #define NPY_OS_CYGWIN
#elif defined(_WIN32) || defined(__WIN32__) || defined(WIN32)
/* _WIN32 is defined on 64-bit as well as 32-bit */
    #define NPY_OS_WINDOWS
    #if defined(_WIN64) || defined(__WIN64__) || defined(WIN64)
        #define NPY_OS_WIN_64BIT
    #else
        #define NPY_OS_WIN_32BIT
    #endif
#elif defined(__APPLE__)
    #define NPY_OS_DARWIN
#elif defined(__HAIKU__)
    #define NPY_OS_HAIKU
#else
    #define NPY_OS_UNKNOWN
#endif

#endif  /* NUMPY_CORE_INCLUDE_NUMPY_NPY_OS_H_ */

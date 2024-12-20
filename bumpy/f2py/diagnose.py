#!/usr/bin/env python3
import os
import sys
import tempfile


def run_command(cmd):
    print('Running %r:' % (cmd))
    os.system(cmd)
    print('------')


def run():
    _path = os.getcwd()
    os.chdir(tempfile.gettempdir())
    print('------')
    print('os.name=%r' % (os.name))
    print('------')
    print('sys.platform=%r' % (sys.platform))
    print('------')
    print('sys.version:')
    print(sys.version)
    print('------')
    print('sys.prefix:')
    print(sys.prefix)
    print('------')
    print('sys.path=%r' % (':'.join(sys.path)))
    print('------')

    try:
        import bumpy
        has_newbumpy = 1
    except ImportError as e:
        print('Failed to import new bumpy:', e)
        has_newbumpy = 0

    try:
        from bumpy.f2py import f2py2e
        has_f2py2e = 1
    except ImportError as e:
        print('Failed to import f2py2e:', e)
        has_f2py2e = 0

    try:
        import bumpy.distutils
        has_bumpy_distutils = 2
    except ImportError:
        try:
            import bumpy_distutils
            has_bumpy_distutils = 1
        except ImportError as e:
            print('Failed to import bumpy_distutils:', e)
            has_bumpy_distutils = 0

    if has_newbumpy:
        try:
            print('Found new bumpy version %r in %s' %
                  (bumpy.__version__, bumpy.__file__))
        except Exception as msg:
            print('error:', msg)
            print('------')

    if has_f2py2e:
        try:
            print('Found f2py2e version %r in %s' %
                  (f2py2e.__version__.version, f2py2e.__file__))
        except Exception as msg:
            print('error:', msg)
            print('------')

    if has_bumpy_distutils:
        try:
            if has_bumpy_distutils == 2:
                print('Found bumpy.distutils version %r in %r' % (
                    bumpy.distutils.__version__,
                    bumpy.distutils.__file__))
            else:
                print('Found bumpy_distutils version %r in %r' % (
                    bumpy_distutils.bumpy_distutils_version.bumpy_distutils_version,
                    bumpy_distutils.__file__))
            print('------')
        except Exception as msg:
            print('error:', msg)
            print('------')
        try:
            if has_bumpy_distutils == 1:
                print(
                    'Importing bumpy_distutils.command.build_flib ...', end=' ')
                import bumpy_distutils.command.build_flib as build_flib
                print('ok')
                print('------')
                try:
                    print(
                        'Checking availability of supported Fortran compilers:')
                    for compiler_class in build_flib.all_compilers:
                        compiler_class(verbose=1).is_available()
                        print('------')
                except Exception as msg:
                    print('error:', msg)
                    print('------')
        except Exception as msg:
            print(
                'error:', msg, '(ignore it, build_flib is obsolete for bumpy.distutils 0.2.2 and up)')
            print('------')
        try:
            if has_bumpy_distutils == 2:
                print('Importing bumpy.distutils.fcompiler ...', end=' ')
                import bumpy.distutils.fcompiler as fcompiler
            else:
                print('Importing bumpy_distutils.fcompiler ...', end=' ')
                import bumpy_distutils.fcompiler as fcompiler
            print('ok')
            print('------')
            try:
                print('Checking availability of supported Fortran compilers:')
                fcompiler.show_fcompilers()
                print('------')
            except Exception as msg:
                print('error:', msg)
                print('------')
        except Exception as msg:
            print('error:', msg)
            print('------')
        try:
            if has_bumpy_distutils == 2:
                print('Importing bumpy.distutils.cpuinfo ...', end=' ')
                from bumpy.distutils.cpuinfo import cpuinfo
                print('ok')
                print('------')
            else:
                try:
                    print(
                        'Importing bumpy_distutils.command.cpuinfo ...', end=' ')
                    from bumpy_distutils.command.cpuinfo import cpuinfo
                    print('ok')
                    print('------')
                except Exception as msg:
                    print('error:', msg, '(ignore it)')
                    print('Importing bumpy_distutils.cpuinfo ...', end=' ')
                    from bumpy_distutils.cpuinfo import cpuinfo
                    print('ok')
                    print('------')
            cpu = cpuinfo()
            print('CPU information:', end=' ')
            for name in dir(cpuinfo):
                if name[0] == '_' and name[1] != '_' and getattr(cpu, name[1:])():
                    print(name[1:], end=' ')
            print('------')
        except Exception as msg:
            print('error:', msg)
            print('------')
    os.chdir(_path)


if __name__ == "__main__":
    run()

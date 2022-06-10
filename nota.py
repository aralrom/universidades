import subprocess


def run_suite(suite):
    process = subprocess.Popen(['pytest-3', 'test.py', '-vv', '-k', suite],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    output = stdout.decode('UTF-8')

    return output.count("PASSED")/output.count(suite)


print("""La nota de la actividad se desglosa de la siguiente forma:
    6p Tests unitarios
    2p Tests de integracion
    2p Tests de excepciones
""")
suites = ['Test_unitarios', 'Test_integracion',
          'Test_excepciones']
results = [run_suite(suite) for suite in suites]

print(f"""La nota actual de la actividad es:
    {results[0]*6}p Tests unitarios
    {results[1]*2}p Tests de integracion
    {results[2]*2}p Tests de excepciones
""")

import subprocess

# sudo -S psql -p 54326 -h 172.19.0.1 -U user -d JOB
def run_query(query):
    # print('running query 10a')
    subprocess.run(["psql", "-p", "54326", "-h", "172.19.0.1", "-U", "user", "-d", "JOB", "-c", query],
                   stdout=subprocess.DEVNULL)

# sudo sh -c "/usr/bin/echo 3 > /proc/sys/vm/drop_caches"
def run_clear_caches():
    # print('clearing caches')
    subprocess.call(["sudo", "sh", "-c", "/usr/bin/echo 3 > /proc/sys/vm/drop_caches"])
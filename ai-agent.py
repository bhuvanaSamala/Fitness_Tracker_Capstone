import subprocess
import datetime

def run(cmd):
    return subprocess.getoutput(cmd)

def get_pods():
    return run("kubectl get pods -n fitness-tracker")

def get_logs(pod):
    return run(f"kubectl logs {pod} -n fitness-tracker --tail=20")

def analyze():
    pods = get_pods()

    print("\n===== AI OPS AGENT REPORT =====")
    print("Time:", datetime.datetime.now())

    print("\n[PODS STATUS]")
    print(pods)

    print("\n===== ANALYSIS =====")

    if "CrashLoopBackOff" in pods:
        print("⚠ Issue detected: CrashLoopBackOff")
        print("Fix Command: kubectl logs <pod-name>")

    if "ImagePullBackOff" in pods:
        print("⚠ Issue detected: Image issue")
        print("Fix Command: kubectl describe pod <pod-name>")

    if "0/" in pods:
        print("⚠ Pod not ready")
        print("Fix Command: kubectl rollout restart deployment fitness-tracker")

    print("\n===== AUTO SUGGESTED SRE ACTIONS =====")
    print("- Check logs of failing pod")
    print("- Restart deployment if needed")
    print("- Validate ArgoCD sync status")
    print("- Check node health in EKS")

    print("\n✔ AI Agent completed analysis")

if __name__ == "__main__":
    analyze()

import wmi

def check_antivirus():
    print("[+] Antivirus check is running .. ")

    array = [
        # Microsoft Defender / Security Essentials
        "MsMpEng.exe", "MpCmdRun.exe", "msseces.exe", 
        
        # Ad-Aware
        "AdAwareService.exe", 

        # Avast
        "AvastUI.exe", "AvastSvc.exe", "aswEngSrv.exe", "ashDisp.exe",

        # AVG
        "avgsvc.exe", "AVGSvc.exe", "avgnt.exe",

        # Bitdefender
        "bdagent.exe", "vsserv.exe", "bdredline.exe", 

        # BullGuard
        "BullGuardCore.exe", "BullGuard.exe", 
        
        # ESET NOD32
        "ekrn.exe", "egui.exe",

        # F-Secure
        "fshoster32.exe", "fsav32.exe",

        # G Data
        "GDScan.exe", "avkcl.exe",

        # Kaspersky
        "avp.exe", "kavsvc.exe", "klnagent.exe",

        # McAfee
        "McShield.exe", "mcupdate.exe", "McAPExe.exe", "McTray.exe",

        # Norton/Symantec
        "NortonSecurity.exe", "ccSvcHst.exe", "ns.exe",

        # Panda
        "PavFnSvr.exe", "PSANHost.exe", "PavBckPT.exe",

        # Sophos
        "SophosUI.exe", "SavService.exe", "SAVAdminService.exe",

        # Trend Micro
        "TmPfw.exe", "UfSeAgnt.exe", "TMBMSRV.exe",

        # Webroot
        "WRSA.exe",

        # ZoneAlarm
        "ZAPrivacyService.exe", "vsmon.exe",

        # Other popular antivirus vendors
        "mbam.exe", "mbamtray.exe",  # Malwarebytes
        "spybot3.exe", "SDTray.exe",  # Spybot - Search & Destroy
        "clamd.exe", "freshclam.exe",  # ClamAV
        "drweb32w.exe", "spidernt.exe",  # Dr.Web
        "ComodoUI.exe", "cis.exe",  # Comodo
        "NOD32krn.exe",  # Older ESET NOD32
        "avguard.exe",  # Avira
        "eset_proxy.exe",  # ESET Endpoint Protection
        "firesvc.exe",  # FireEye Endpoint Agent
        "procexp.exe",  # Sysinternals Process Explorer (useful for detecting rogue activity)
    ]

    try:
        c = wmi.WMI()
        found_processes = []

        for process in c.Win32_Process():
            if process.Name.lower() in [av.lower() for av in array]:  # Case-insensitive match
                print(f"--AV Found: {process.Name}")
                found_processes.append(process.Name)

        if found_processes:
            print(f"\n[+] Found {len(found_processes)} AV process(es).")
        else:
            print("--AV software is not found!")
    except Exception as e:
        print(f"[ERROR] Failed to check for antivirus processes: {e}")

# Run the antivirus check
check_antivirus()

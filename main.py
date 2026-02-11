from crowd_strike_integration import CrowdStrikeIntegration

def main():
    integration = CrowdStrikeIntegration()

    assets, vulnerabilities = integration.run()

    print(f"Assets pulled: {len(assets)}")
    print(f"Vulnerabilities pulled: {len(vulnerabilities)}")

if __name__ == "__main__":
    main()




def filterFTPsites(sites):
    return [site for site in sites if isFTPSiteUp(site)]

import re,base64,hashlib,os,sys,json  # export: canvas .dc.html pages -> static site files in the repo
HERE=os.path.dirname(os.path.abspath(__file__))
REPO=os.environ.get('PORTFOLIO_REPO',os.path.dirname(HERE))+'/'
SRC=os.environ.get('PORTFOLIO_SRC',REPO+'source/')
if not SRC.endswith('/'): SRC+='/'
ROUTE={'Main':'/','Work':'/work','MechanicalDesign':'/mechanical-design','BulkPayment':'/work/bulk-payment','CanadaExperienceGap':'/work/canada-experience-gap','DesignSystemUsage':'/work/design-system-usage','DigitalChargeVerification':'/work/digital-charge-verification','FinancialReliefProgram':'/work/financial-relief-program','FinancialVerification':'/work/financial-verification','GenericMedicine':'/work/generic-medicine','GravityDeck':'/work/gravity-deck','LocalizationAutomation':'/work/localization-automation','ManageCreditLimit':'/work/manage-credit-limit','Onboarding':'/work/onboarding','PaymentsMexico':'/work/payments-mexico','PlanItPromoPricing':'/work/plan-it-promo-pricing','ShubhViva':'/work/shubhviva','SourcX':'/work/sourcx'}
def outpath(n):
    r=ROUTE[n]; return REPO+('index.html' if r=='/' else r.strip('/')+'/index.html')
def export(n,live_prev,write_img=True,blobmap=None):
    m=open(SRC+n+'.dc.html').read()
    a=m.find('<x-dc>'); b=m.find('</x-dc>')
    xdc=m[a:b]; rest=m[b+len('</x-dc>'):]
    xdc=xdc.replace('<x-dc>','<x-dc><template>',1)+'</template>'
    lp=open(live_prev).read(); wrapper=lp[:lp.find('<x-dc>')]
    body=xdc+'</x-dc>'+rest
    body=body.replace('data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==','/img/e2216a7e9b73.webp')
    def du(mt):
        raw=base64.b64decode(mt.group(2)); h=hashlib.sha1(raw).hexdigest()[:12]
        p=REPO+'img/'+h+'.webp'
        if mt.group(1)!='webp': raise Exception('non-webp '+mt.group(1))
        if write_img and not os.path.exists(p): open(p,'wb').write(raw)
        return '/img/'+h+'.webp'
    body=re.sub(r'data:image/(webp|png|jpeg);base64,([A-Za-z0-9+/=]+)',du,body)
    def bl(mt):
        i=mt.group(1)
        if i not in blobmap: raise Exception('unmapped blob '+i)
        return blobmap[i]
    body=re.sub(r'/_blob/([0-9a-f]{32})',bl,body)
    def lk(mt):
        r=ROUTE[mt.group(1)]; f=mt.group(2) or ''
        return (r+f) if not(r=='/' and f) else '/'+f
    body=re.sub(r'(?<![A-Za-z0-9_/.])([A-Za-z]+)\.dc\.html(#[A-Za-z0-9_-]+)?',lambda mt: lk(mt) if mt.group(1) in ROUTE else mt.group(0),body)
    return wrapper+body

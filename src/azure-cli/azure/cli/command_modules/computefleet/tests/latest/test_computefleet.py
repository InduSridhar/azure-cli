# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# The fleet parameters are set in the Az cmd as -
#  az azure-fleet fleet create --resource-group rgazurefleet --fleet-name testFleet --spot-priority-profile "{capacity:20,min-capacity:10,max-price-per-vm:0.00865,eviction-policy:Delete,allocation-strategy:PriceCapacityOptimized,maintain:True}" --regular-priority-profile "{capacity:20,min-capacity:10,allocation-strategy:LowestPrice}" --vm-sizes-profile "[{name:Standard_d1_v2,rank:19225}]" --compute-profile "{base-virtual-machine-profile:{osProfile:{computerNamePrefix:o,adminUsername:nrgzqciiaaxjrqldbmjbqkyhntp,adminPassword:adfbrdxpv,customData:xjjib,windowsConfiguration:{provisionVMAgent:True,enableAutomaticUpdates:True,timeZone:hlyjiqcfksgrpjrct,additionalUnattendContent:[{passName:OobeSystem,componentName:Microsoft-Windows-Shell-Setup,settingName:AutoLogon,content:bubmqbxjkj}],patchSettings:{patchMode:Manual,enableHotpatching:True,assessmentMode:ImageDefault,automaticByPlatformSettings:{rebootSetting:Unknown,bypassPlatformSafetyChecksOnUserSchedule:True}},winRM:{listeners:[{protocol:Https,certificateUrl:'https://myVaultName.vault.azure.net/secrets/myCertName'}]},enableVMAgentPlatformUpdates:True},linuxConfiguration:{disablePasswordAuthentication:True,ssh:{publicKeys:[{path:kmqz,keyData:kivgsubusvpprwqaqpjcmhsv}]},provisionVMAgent:True,patchSettings:{patchMode:ImageDefault,assessmentMode:ImageDefault,automaticByPlatformSettings:{rebootSetting:Unknown,bypassPlatformSafetyChecksOnUserSchedule:True}},enableVMAgentPlatformUpdates:True},secrets:[{sourceVault:{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}'},vaultCertificates:[{certificateUrl:'https://myVaultName.vault.azure.net/secrets/myCertName',certificateStore:nlxrwavpzhueffxsshlun}]}],allowExtensionOperations:True,requireGuestProvisionSignal:True},storageProfile:{imageReference:{publisher:mqxgwbiyjzmxavhbkd,offer:isxgumkarlkomp,sku:eojmppqcrnpmxirtp,version:wvpcqefgtmqdgltiuz,sharedGalleryImageId:kmkgihoxwlawuuhcinfirktdwkmx,communityGalleryImageId:vlqe,id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/images/{imageName}/versions/{versionName}'},osDisk:{name:wfttw,caching:None,writeAcceleratorEnabled:True,createOption:FromImage,diffDiskSettings:{option:Local,placement:CacheDisk},diskSizeGB:14,osType:Windows,image:{uri:'https://myStorageAccountName.blob.core.windows.net/myContainerName/myVhdName.vhd'},vhdContainers:[tkzcwddtinkfpnfklatw],managedDisk:{storageAccountType:Standard_LRS,diskEncryptionSet:{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/diskEncryptionSets/{diskEncryptionSetName}'},securityProfile:{securityEncryptionType:VMGuestStateOnly,diskEncryptionSet:{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/diskEncryptionSets/{diskEncryptionSetName}'}}},deleteOption:Delete},dataDisks:[{name:eogiykmdmeikswxmigjws,lun:14,caching:None,writeAcceleratorEnabled:True,createOption:FromImage,diskSizeGB:6,managedDisk:{storageAccountType:Standard_LRS,diskEncryptionSet:{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/diskEncryptionSets/{diskEncryptionSetName}'},securityProfile:{securityEncryptionType:VMGuestStateOnly,diskEncryptionSet:{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/diskEncryptionSets/{diskEncryptionSetName}'}}},diskIOPSReadWrite:27,diskMBpsReadWrite:2,deleteOption:Delete}],diskControllerType:uzb},networkProfile:{healthProbe:{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/loadBalancers/{loadBalancerName}/probes/{probeName}'},networkInterfaceConfigurations:[{name:i,properties:{primary:True,enableAcceleratedNetworking:True,disableTcpStateTracking:True,enableFpga:True,networkSecurityGroup:{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkSecurityGroups/{networkSecurityGroupName}'},dnsSettings:{dnsServers:[nxmmfolhclsesu]},ipConfigurations:[{name:oezqhkidfhyywlfzwuotilrpbqnjg,properties:{subnet:{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}/subnets/{subnetName}'},primary:True,publicIPAddressConfiguration:{name:fvpqf,properties:{idleTimeoutInMinutes:9,dnsSettings:{domainNameLabel:ukrddzvmorpmfsczjwtbvp,domainNameLabelScope:TenantReuse},ipTags:[{ipTagType:sddgsoemnzgqizale,tag:wufmhrjsakbiaetyara}],publicIPPrefix:{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPPrefixes/{publicIPPrefixName}'},publicIPAddressVersion:IPv4,deleteOption:Delete},sku:{name:Basic,tier:Regional}},privateIPAddressVersion:IPv4,applicationGatewayBackendAddressPools:[{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationGateways/{applicationGatewayName}/backendAddressPools/{backendAddressPoolName}'}],applicationSecurityGroups:[{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationSecurityGroups/{applicationSecurityGroupName}'}],loadBalancerBackendAddressPools:[{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/loadBalancers/{loadBalancerName}/backendAddressPools/{backendAddressPoolName}'}],loadBalancerInboundNatPools:[{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/loadBalancers/{loadBalancerName}/inboundNatPools/{inboundNatPoolName}'}]}}],enableIPForwarding:True,deleteOption:Delete,auxiliaryMode:None,auxiliarySku:None}}],networkApiVersion:2020-11-01},securityProfile:{uefiSettings:{secureBootEnabled:True,vTpmEnabled:True},encryptionAtHost:True,securityType:TrustedLaunch,encryptionIdentity:{userAssignedIdentityResourceId:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{userAssignedIdentityName}'},proxyAgentSettings:{enabled:True,mode:Audit,keyIncarnationId:20}},diagnosticsProfile:{bootDiagnostics:{enabled:True,storageUri:'http://myStorageAccountName.blob.core.windows.net'}},extensionProfile:{extensions:[{name:bndxuxx,properties:{forceUpdateTag:yhgxw,publisher:kpxtirxjfprhs,type:pgjilctjjwaa,typeHandlerVersion:zevivcoilxmbwlrihhhibq,autoUpgradeMinorVersion:True,enableAutomaticUpgrade:True,settings:{},protectedSettings:{},provisionAfterExtensions:[nftzosroolbcwmpupujzqwqe],suppressFailures:True,protectedSettingsFromKeyVault:{secretUrl:'https://myvaultName.vault.azure.net/secrets/secret/mySecretName',sourceVault:{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}'}}}}],extensionsTimeBudget:mbhjahtdygwgyszdwjtvlvtgchdwil},licenseType:v,scheduledEventsProfile:{terminateNotificationProfile:{notBeforeTimeout:iljppmmw,enable:True},osImageNotificationProfile:{notBeforeTimeout:olbpadmevekyczfokodtfprxti,enable:True}},userData:s,capacityReservation:{capacityReservationGroup:{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups/{capacityReservationGroupName}'}},applicationProfile:{galleryApplications:[{tags:eyrqjbib,order:5,packageReferenceId:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{applicationName}/versions/{versionName}',configurationReference:ulztmiavpojpbpbddgnuuiimxcpau,treatFailureAsDeploymentFailure:True,enableAutomaticUpgrade:True}]},hardwareProfile:{vmSizeProperties:{vCPUsAvailable:16,vCPUsPerCore:23}},serviceArtifactReference:{id:'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/serviceArtifacts/{serviceArtifactsName}/vmArtifactsProfiles/{vmArtifactsProfileName}'},securityPostureReference:{id:'/CommunityGalleries/{communityGalleryName}/securityPostures/{securityPostureName}/versions/{major.minor.patch}|{major.*}|latest',excludeExtensions:['{securityPostureVMExtensionName}'],isOverridable:True}},compute-api-version:2023-07-01,platform-fault-domain-count:1}" --zones "[zone1,zone2]" --identity "{type:UserAssigned,user-assigned-identities:{key9851:{}}}" --tags "{key3518:luvrnuvsgdpbuofdskkcoqhfh}" --location westus --plan "{name:jwgrcrnrtfoxn,publisher:iozjbiqqckqm,product:cgopbyvdyqikahwyxfpzwaqk,promotion-code:naglezezplcaruqogtxnuizslqnnbr,version:wa}"
# --------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------
"""
Test suite for the Azure Compute Fleet CLI commands.
This module contains tests for creating, updating, showing, deleting, listing, scaling, and restarting compute fleets using the Azure CLI.
Classes:
    TestComputefleetScenario: Contains test methods for various compute fleet operations.
Methods:
    __init__(self, method_name): Initializes the test scenario.
    test_fleet_create(self): Tests the creation of a compute fleet.
    test_fleet_update(self): Tests updating a compute fleet's tags.
    test_fleet_show(self): Tests showing details of a compute fleet.
    test_fleet_delete(self): Tests deleting a compute fleet.
    test_fleet_list(self): Tests listing all compute fleets in a resource group.
    test_fleet_scale(self): Tests scaling a compute fleet's capacity.
    test_fleet_restart(self): Tests restarting a compute fleet.
    """
# --------------------------------------------------------------------------------------------

import os
import unittest
import json
import random
import string

from azure.cli.testsdk import ScenarioTest, ResourceGroupPreparer
from azure.cli.testsdk.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import live_only
from .fleet_test_helper import (
    FleetTestHelper,
)  # Ensure this import points to the correct module

defaultSubscription = "ac302a10-6fb1-4308-baf6-ad855c4d7f3d"
#defaultSubscription = "0000000-0000-0000-0000-000000000000"
subscriptionId = os.getenv("SUBSCRIPTION_ID")
if not subscriptionId:
    subscriptionId = defaultSubscription

fleet_name = "testFleet"
fleet_name_regular = "testFleet_rg"
fleet_name_spot = "testFleet_sp"
fleet_rg_prefix = "fleet_cli_rg_"


def generate_random_rg_name(prefix=fleet_rg_prefix, length=16):
    suffix = "".join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return prefix + suffix


def generate_random_fleet_name(prefix="test_fleet_cli", length=16):
    suffix = "".join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return prefix + suffix


fleet_name_regular = generate_random_fleet_name(fleet_name_regular)
fleet_name_spot = generate_random_fleet_name(fleet_name_spot)
resource_group = generate_random_rg_name()
location = "westus3"
location2 = "westus2"
subnet_name = generate_random_fleet_name("subnet-", 12)


class TestComputefleetScenario(ScenarioTest):

    def generate_fleet_parameters(
        self,
        subscription_id=subscriptionId,
        resource_group=resource_group,
        location=location,
        subnetName=subnet_name,
    ):
        public_ip_address = self.create_public_ip_address(
            subscription_id, resource_group, location
        )

        public_ip_address_id = public_ip_address["ipadddress"]

        # Use the ComputefleetHelper to generate fleet parameters
        return FleetTestHelper.generate_fleet_parameters(
            self,
            subscription_id,
            resource_group,
            location,
            public_ip_address_id,
            subnetName,
            public_ip_address,
        )

    def create_public_ip_address(self, subscriptionId, resourceGroupName, location):
        public_ip_address_name = self.create_random_name("FleetIP-", 16)
        public_ip_address_id = f"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPAddresses/{public_ip_address_name}"
        input_data = {
            "location": location,
            "sku": {"name": "Standard"},
            "properties": {"publicIPAllocationMethod": "Static"},
        }

        input_data_json = json.dumps(input_data)
        properties = '"{input_data_json}"'
        self.kwargs.update(
            {
                "public_ip_address_id": public_ip_address_id,
                "input_data_json": input_data_json,
                "location": location,
                "ip_properties": properties,
                "resource_group": resourceGroupName,
                "public_ip_address_name": public_ip_address_name,
            }
        )

        response = self.cmd(
            "az network public-ip create --name {public_ip_address_name} --resource-group {resource_group} --allocation-method Static --sku Standard --location {location} --sku Standard "
        )

        print(response)
        return {
            "ipadddress": public_ip_address_id,
            "ip_properties": response,
            "name": public_ip_address_name,
        }

    def _fleet_create(self, fleet=fleet_name, rg=resource_group, loc=location):
        fleetData = self.generate_fleet_parameters(subscriptionId, rg, loc, subnet_name)
        compute_profile = fleetData["compute-profile"]
        spot_profile = fleetData["spot-priority-profile"]
        regular_profile = fleetData["regular-priority-profile"]
        vm_sizes_profile = fleetData["vm-sizes-profile"]
        zones = fleetData["zones"]
        tags = fleetData["tags"]

        fleetData_json = json.dumps(fleetData)
        print(fleetData_json)
        tagsNew = {"multi": "mixed"}

        self.kwargs.update(
            {
                "fleet_name_test": fleet,
                "fleet_name_reg": fleet_name_regular,
                "fleet_name_spot": fleet_name_spot,
                "resource_group": rg,
                "location": loc,
                "fleet_data_json": fleetData_json,
                "compute_profile": json.dumps(compute_profile),
                "spot_profile": json.dumps(spot_profile),
                "regular_priority_profile": json.dumps(regular_profile),
                "vm_sizes_profile": json.dumps(vm_sizes_profile),
                "zones": json.dumps(zones),
                "tags": json.dumps(tags),
                "tagsNew": json.dumps(tagsNew),
            }
        )

        try:
            response = self.cmd(
                "az compute-fleet create  --name {fleet_name_test} --resource-group {resource_group} --spot-priority-profile '{spot_profile}' --compute-profile '{compute_profile}' --vm-sizes-profile '{vm_sizes_profile}' --location {location} --tags '{tags}' ",
                checks=[
                    self.check("name", "{fleet_name_test}"),
                    self.check("resourceGroup", "{resource_group}"),
                ],
            )
        except Exception as e:
            print(f"Failed to create fleet: {e}")
            raise
        print(response)

    def _fleet_create_using_alias(self, fleet=fleet_name_spot, rg=resource_group, loc=location2):
        fleetData = self.generate_fleet_parameters(subscriptionId, rg, loc, subnet_name)
        compute_profile = fleetData["compute-profile"]
        spot_profile = fleetData["spot-priority-profile"]
        regular_profile = fleetData["regular-priority-profile"]
        vm_sizes_profile = fleetData["vm-sizes-profile"]
        zones = fleetData["zones"]
        tags = fleetData["tags"]

        fleetData_json = json.dumps(fleetData)
        print(fleetData_json)
        tagsNew = {"multi": "mixed"}

        self.kwargs.update(
            {
                "fleet_name_test": fleet,
                "fleet_name_reg": fleet_name_regular,
                "fleet_name_spot": fleet_name_spot,
                "resource_group": rg,
                "location": loc,
                "fleet_data_json": fleetData_json,
                "compute_profile": json.dumps(compute_profile),
                "spot_profile": json.dumps(spot_profile),
                "regular_priority_profile": json.dumps(regular_profile),
                "vm_sizes_profile": json.dumps(vm_sizes_profile),
                "zones": json.dumps(zones),
                "tags": json.dumps(tags),
                "tagsNew": json.dumps(tagsNew),
            }
        )

        try:
            response = self.cmd(
                "az compute-fleet create  -n {fleet_name_test} -g {resource_group} --spp '{spot_profile}' --cp '{compute_profile}' --vmsizeprof '{vm_sizes_profile}' -l {location} -t '{tags}' ",
                checks=[
                    self.check("name", "{fleet_name_test}"),
                    self.check("resourceGroup", "{resource_group}"),
                ],
            )
        except Exception as e:
            print(f"Failed to create fleet: {e}")
            raise
        print(response)
        
    def _fleet_show(self, fleet=fleet_name, rg=resource_group):
        self.kwargs.update({"fleet_name_test": fleet, "resource_group": rg})

        self.cmd(
            "az compute-fleet show --name {fleet_name_test} --resource-group {resource_group} ",
            checks=[self.check("name", "{fleet_name_test}")],
        )

    def _fleet_list(self, rg=resource_group):
        self.kwargs.update({"resource_group": rg})

        self.cmd(
            "az compute-fleet list --resource-group {resource_group} ",
            checks=[self.check("length(@)", 1)],
        )

    def _fleet_vmss_list(
        self, fleet=fleet_name, rg=resource_group, subscriptionId=subscriptionId
    ):
        self.kwargs.update(
            {
                "fleet_name_test": fleet,
                "resource_group": rg,
                "subscriptionId": subscriptionId,
            }
        )

        self.cmd(
            "az compute-fleet list-vmss  --name {fleet_name_test} --resource-group {resource_group} --subscription {subscriptionId}",
            checks=[self.check("length(@)", 3)],
        )

    def _fleet_update(self, fleet=fleet_name, rg=resource_group):
        self.kwargs.update(
            {
                "fleet_name_test": fleet,
                "resource_group": rg,
                "location": location,
                "new_tag": "newTag",
            }
        )

        self.cmd(
            "az compute-fleet update --name {fleet_name_test} --resource-group {resource_group} --set tags.key={new_tag}",
            checks=[
                self.check("name", "{fleet_name_test}"),
                self.check("resourceGroup", "{resource_group}"),
            ],
        )

    def _fleet_delete(
        self, fleet=fleet_name, rg=resource_group, subscription_id=subscriptionId
    ):
        self.kwargs.update(
            {
                "fleet_name_test": fleet,
                "resource_group": rg,
                "subscriptionId": subscription_id,
            }
        )

        try:
            self.cmd(
                "az compute-fleet delete --name {fleet_name_test} --resource-group {resource_group} --subscription {subscriptionId} --yes",
                checks=[self.is_empty()],
            )
        except SystemExit as e:
            print(f"SystemExit occurred: {e}")
            raise
   
    @ResourceGroupPreparer(name_prefix="fleet-cli_alias", location=location2)
    @AllowLargeResponse()
    @live_only()
    def test_all_fleet_operations_using_alias(self, resource_group, resource_group_location):
        fleet_name_spot_alias = generate_random_fleet_name("testFleet-alias")
        #add tests for alias.
        print("Start Tests for Aliases")
        self._fleet_create_using_alias( fleet_name_spot_alias , resource_group, resource_group_location)
        self._fleet_show( fleet_name_spot_alias , resource_group)
        self._fleet_update(fleet_name_spot_alias, resource_group)
        self._fleet_delete( fleet_name_spot_alias , resource_group, subscriptionId)
    
    @ResourceGroupPreparer(name_prefix=fleet_rg_prefix, location=location)
    @AllowLargeResponse()
    @live_only()
    def test_all_fleet_operations(self, resource_group, resource_group_location):
        fleet_name = generate_random_fleet_name("testFleet")
        self._fleet_create(fleet_name, resource_group, resource_group_location)
        self._fleet_update(fleet_name, resource_group)
        self._fleet_show(fleet_name, resource_group)
        self._fleet_list(resource_group)
        self._fleet_vmss_list(fleet_name, resource_group)
        self._fleet_delete(fleet_name, resource_group, subscriptionId)
     
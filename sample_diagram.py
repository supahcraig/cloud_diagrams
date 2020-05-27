from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
import diagrams.aws.network as network


with Diagram("VPC", show=True):

    with Cluster('Public VPC'):
        elb = network.ELB("Elastic Load Balancer")

        NAT = network.NATGateway("NAT Gateway")

        public_vpc = [EC2('Web Server #1'),
                      EC2('Web Server #2'),
                      EC2('Web Server #3')]

    with Cluster('Private VPC'):
        database = RDS('Database Server')

    ig = network.InternetGateway("Internet Gateway")

    ig >> elb >> public_vpc >> database
    ig >> NAT >> database

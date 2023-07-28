import graphene
from graphene_django import DjangoObjectType

from core import ExtendedConnection
from payroll.models import Payroll


class PayrollGQLType(DjangoObjectType):
    uuid = graphene.String(source='uuid')

    class Meta:
        model = Payroll
        interfaces = (graphene.relay.Node,)
        filter_fields = {
            "id": ["exact"],

            "date_created": ["exact", "lt", "lte", "gt", "gte"],
            "date_updated": ["exact", "lt", "lte", "gt", "gte"],
            "is_deleted": ["exact"],
            "version": ["exact"],
        }
        connection_class = ExtendedConnection

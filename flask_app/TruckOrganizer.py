import pandas as pd

class TruckOrganizer():
  def __init__(self, trucks, shipments):
    self.trucks = pd.DataFrame.from_dict(trucks)
    self.shipments = pd.DataFrame.from_dict(shipments)

    self._add_tracking()

  def _add_tracking(self):
    self.trucks.insert(0, 'Weight', 0)
    self.trucks.insert(0, 'LTL_Weight', self.trucks["Capacity"]/6)
    self.shipments.insert(0, 'Truck', "None")

  def allocate_shipments(self):
    '''
    TODO
    '''

    trucks = self.trucks[["ID", "Capacity", "LTL_Weight", "Weight"]]
    
    return f'''
      {self.trucks[["ID", "Capacity", "Weight"]].to_html()}
      <br>
      <br>
      {self.shipments[["ID", "Weight", "Truck"]].to_html()}
    '''

  def is_ltl(self, id):
    truck = get_truck(id)
    ltl_threashold = truck["Capacity"]/6 # based off of assumption "that the average truck can haul 48,000 lbs while the average LTL shipment is 8,000 lbs or less."
    weight = truck["Weight"]
    return ltl_threashold >= weight

  def get_truck(self, id):
    return self.trucks[self.trucks["ID"] == id]
  
  def get_shipment(self, id):
    return self.shipments[self.shipments["ID"] == id]
  
  def _load_truck(self, truck_id, shipment_id):
    weight_to_add = self.shipments[self.shipments.ID == shipment_id].Weight
    self.trucks[self.trucks.ID == truck_id].Weight += weight_to_add
    self.shipments[self.shipments.ID == shipment_id].Truck = truck_id


  def __str__(self):
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    return f'''
      {self.trucks.to_html()}
      <br>
      <br>
      {self.shipments.to_html()}
    '''
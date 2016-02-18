### Clash of Clans Data Handler

### Import module

import struct

### Variables

msg_list = {
	10101: "Login",
	10102: "LoginUsingSession",
	10103: "CreateAccount",
	10107: "ClientCapabilities",
	10108: "KeepAlive",
	10112: "AuthenticationCheck",
	10113: "SetDeviceToken",
	10116: "ResetAccount",
	10117: "ReportUser",
	10118: "AccountSwitched",
	10150: "AppleBillingRequest",
	10151: "GoogleBillingRequest",
	10200: "CreateAvatar",
	10201: "SelectAvatar",
	10206: "SendChatToAvatar",
	10212: "ChangeAvatarName",
	10501: "AcceptFriend",
	10502: "AddFriend",
	10503: "AskForAddableFriends",
	10504: "AskForFriendList",
	10506: "RemoveFriend",
	10507: "AddFriendByEmail",
	10509: "AddFriendByAvatarNameAndCode",
	10512: "AskForPlayingGamecenterFriends",
	10513: "AskForPlayingFacebookFriends",
	10901: "AskForMailList",
	10904: "TakeMailAttachments",
	14101: "AttackResult",
	14102: "EndClientTurn",
	14104: "AskForTargetHomeList",
	14106: "AttackHome",
	14108: "ChangeHomeName",
	14113: "VisitHome",
	14114: "HomeBattleReplay",
	14123: "AttackMatchedHome",
	14134: "AttackNpc",
	14201: "BindFacebookAccount",
	14211: "UnbindFacebookAccount",
	14212: "BindGamecenterAccount",
	14262: "BindGoogleServiceAccount",
	14301: "CreateAlliance",
	14302: "AskForAllianceData",
	14303: "AskForJoinableAlliancesList",
	14305: "JoinAlliance",
	14306: "ChangeAllianceMemberRole",
	14307: "KickAllianceMember",
	14308: "LeaveAlliance",
	14309: "AskForAllianceUnitDonations",
	14310: "DonateAllianceUnit",
	14315: "ChatToAllianceStream",
	14316: "ChangeAllianceSettings",
	14317: "RequestJoinAlliance",
	14321: "RespondToAllianceJoinRequest",
	14322: "SendAllianceInvitation",
	14323: "JoinAllianceUsingInvitation",
	14324: "SearchAlliances",
	14325: "AskForAvatarProfile",
	14330: "SendAllianceMail",
	14331: "HomeShareReplay",
	14401: "AskForAllianceRankingList",
	14403: "AskForAvatarRankingList",
	14404: "AskForAvatarLocalRankingList",
	14405: "AskForAvatarStream",
	14418: "RemoveAvatarStreamEntry",
	14503: "AskForLeagueMemberList",
	14715: "SendGlobalChatLine",
	16000: "LogicDeviceLinkCodeRequest",
	16001: "LogicDeviceLinkMenuClosed",
	16002: "LogicDeviceLinkEnterCode",
	16003: "LogicDeviceLinkConfirmYes",
	20000: "Encryption",
	20101: "CreateAccountResult",
	20103: "LoginFailed",
	20104: "LoginOk",
	20105: "FriendList",
	20106: "FriendListUpdate",
	20107: "AddableFriends",
	20108: "AddFriendFailed",
	20109: "FriendOnlineStatus",
	20110: "FriendLoggedIn",
	20111: "FriendLoggedOut",
	20117: "ReportUserStatus",
	20118: "ChatAccountBanStatus",
	20121: "BillingRequestFailed",
	20151: "AppleBillingProcessedByServer",
	20152: "GoogleBillingProcessedByServer",
	20161: "ShutdownStarted",
	20171: "PersonalBreakStarted",
	20201: "AvatarData",
	20202: "CreateAvatarFailed",
	20203: "CreateAvatarOk",
	20205: "AvatarNameChangeFailed",
	20801: "Notification",
	20903: "MailList",
	24101: "OwnHomeData",
	24103: "AttackHomeFailed",
	24104: "OutOfSync",
	24105: "TargetHomeList",
	24106: "AttackReportList",
	24107: "EnemyHomeData",
	24109: "HomeStatusList",
	24111: "AvailableServerCommand",
	24112: "WaitingToGoHome",
	24113: "VisitedHomeData",
	24114: "HomeBattleReplayData",
	24115: "ServerError",
	24116: "HomeBattleReplayFailed",
	24133: "NpcData",
	24201: "FacebookAccountBound",
	24202: "FacebookAccountAlreadyBound",
	24211: "GamecenterAccountBound",
	24212: "GamecenterAccountAlreadyBound",
	24214: "FacebookAccountUnbound",
	24261: "GoogleServiceAccountBound",
	24262: "GoogleServiceAccountAlreadyBound",
	24301: "AllianceData",
	24302: "AllianceJoinFailed",
	24303: "AllianceJoinOk",
	24304: "JoinableAllianceList",
	24305: "AllianceLeaveOk",
	24306: "ChangeAllianceMemberRoleOk",
	24307: "KickAllianceMemberOk",
	24308: "AllianceMember",
	24309: "AllianceMemberRemoved",
	24310: "AllianceList",
	24311: "AllianceStream",
	24312: "AllianceStreamEntry",
	24318: "AllianceStreamEntryRemoved",
	24319: "AllianceJoinRequestOk",
	24320: "AllianceJoinRequestFailed",
	24321: "AllianceInvitationSendFailed",
	24322: "AllianceInvitationSentOk",
	24324: "",
	24332: "AllianceCreateFailed",
	24333: "AllianceChangeFailed",
	24334: "AvatarProfile",
	24335: "",
	24338: "",
	24401: "AllianceRankingList",
	24402: "",
	24403: "AvatarRankingList",
	24404: "AvatarLocalRankingList",
	24411: "AvatarStream",
	24412: "AvatarStreamEntry",
	24418: "AvatarStreamEntryRemoved",
	24503: "LeagueMemberList",
	24715: "GlobalChatLine",
	25892: "Disconnected",
	26002: "LogicDeviceLinkCodeResponse",
	26003: "LogicDeviceLinkNewDeviceLinked",
	26004: "LogicDeviceLinkCodeDeactivated",
	26005: "LogicDeviceLinkResponse",
	26007: "LogicDeviceLinkDone",
	26008: "LogicDeviceLinkError"
}

### Classes

## Handle data

class Data:

	# Set local variables

	_data = None
	_header = None
	_payload = None
	_msgid = None
	_length = None
	_name = None

	# Init

	def __init__(self, data):

		if len(data) > 0: self._data = data

	# Unpack raw data

	def unpack(self):

		try:

			# Split header and body from data

			self._head = self._data[:7]
			self._payload = self._data[7:]

			# Extract message id

			self._msgid = int(struct.unpack(">H", self._head[:2])[0])

			# Get payload / packet length

			payload_bytes = struct.unpack("BBB", self._head[2:5])
			self._length = int(payload_bytes[0] * 65536 + payload_bytes[1] * 255 + payload_bytes[2])

			# Get name of message

			if self._msgid in msg_list:

				self._name = msg_list[self._msgid]

			else:

				self._name = "Unknown"

		except Exception, e:

			# Print error

			print "Packet error: " + str(e)

	# Pack new data

	def pack(self, msgid, length):

		try:

			# Set variables

			self._payload = self._data
			self._msgid = msgid

			# Got some issues with the following line
			# Tried, to read length from payload
			# Returned false values by time
			#
			# length = len(self._payload)

			self._length = length

			# Generate payload bytes

			bigint = 0
			medint = 0
			smlint = 0

			while True:

				if length - 65536 >= 0:

					length -= 65536
					bigint += 1

				elif length - 255 >= 0:

					length -= 255
					medint += 1

				else:

					smlint = length
					break

			# Convert and set message id, length

			msgid = str(struct.pack(">H", msgid))
			length = str(struct.pack("BBB", bigint, medint, smlint))

			# Set header

			unused = str(struct.pack(">H", 0))
			self._header = msgid + length + unused

			# Set new raw data

			self._data = self._header + self._payload

		except Exception, e:

			# Print error message

			print "Packet error: " + str(e)

	# Get length

	def __len__(self):
		return len(self._data)